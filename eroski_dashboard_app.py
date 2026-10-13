import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df_pca = pd.read_csv('Data/datos_dashboard.csv') 
df_top_vol = pd.read_csv('Data/df_top_vol.csv')
df_debate_bloques = pd.read_csv('Data/df_debate_bloques.csv')
tendencia_mensual = pd.read_csv('Data/tendencia_mensual.csv')

COLOR_ROJO = "#e30613"
COLOR_AZUL = "#004B87"

df_pca['Cluster_Label'] = 'Clúster ' + df_pca['cluster'].astype(str)
df_pca = df_pca.sort_values(by='cluster')

df_pca['Tipo de Artículo'] = 'Catálogo'
df_pca.loc[df_pca['es_promo'] == True, 'Tipo de Artículo'] = 'Promoción'

#mapa de clusterización
fig_cluster = px.scatter(
    df_pca, 
    x='pca_x', 
    y='pca_y', 
    color='Cluster_Label',
    facet_col='Cluster_Label', 
    facet_col_wrap=2,
    symbol='Tipo de Artículo',
    hover_data=['descripcion'],
    title="<b>Análisis de Afinidad: Segmentación por Factores Latentes (ALS + PCA)</b>",
    labels={
        'pca_x': 'Factor Latente 1', 
        'pca_y': '', 
        'Cluster_Label': 'Segmento',
        'Tipo de Artículo': 'Leyenda'
    },
    color_discrete_sequence=[COLOR_AZUL, COLOR_ROJO, "#777777", "#28a745"]
)
fig_cluster.update_traces(marker=dict(size=7))
fig_cluster.update_layout(plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=40))

#bloques temporales
fig_bloques = px.bar(
    df_debate_bloques, x='macro_categoria', y='Porcentaje_del_Carro', color='bloque_semana',
    barmode='group', title="<b>Auditoría de Bloques: Lun-Jue vs Vie-Sáb</b>",
    labels={
        'macro_categoria': 'Categoría del Producto', 
        'Porcentaje_del_Carro': '% de Peso en la Cesta',
        'bloque_semana': 'Días'
    },
    color_discrete_map={'Lun-Jue (Diario)': '#777777', 'Vie-Sáb (Finde)': '#e30613'}
)
fig_bloques.update_layout(plot_bgcolor='white', paper_bgcolor='white')

#nómina
fig_nomina = px.line(
    tendencia_mensual, x='dia_del_mes', y='id_transaccion',
    title="<b>Efecto Nómina: Evolución Transaccional del Mes</b>",
    labels={
        'dia_del_mes': 'Día del Mes (1-31)', 
        'id_transaccion': 'Volumen de Tickets Únicos'
    },
    color_discrete_sequence=[COLOR_ROJO], markers=True
)
fig_nomina.update_layout(plot_bgcolor='white', paper_bgcolor='white')

#top 10: motores de tráfico
fig_vol = px.bar(
    df_top_vol, x='unidades', y='descripcion', orientation='h',
    title="<b>Top 10 Productos: Motores de Tráfico Global</b>",
    labels={
        'unidades': 'Total Unidades Vendidas', 
        'descripcion': 'Artículo del Catálogo'
    },
    color_discrete_sequence=[COLOR_AZUL]
)
fig_vol.update_layout(yaxis={'categoryorder':'total ascending'}, plot_bgcolor='white', paper_bgcolor='white')


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Estratégico Retail - Eroski", style={'textAlign': 'center', 'color': COLOR_AZUL}),
    
    html.Div([dcc.Graph(figure=fig_cluster)]),
    
    html.Div([
        html.Div([dcc.Graph(figure=fig_bloques)], style={'width': '50%'}),
        html.Div([dcc.Graph(figure=fig_nomina)], style={'width': '50%'})
    ], style={'display': 'flex'}),
    
    html.Div([dcc.Graph(figure=fig_vol)])
])

if __name__ == '__main__':
    app.run(debug=True)