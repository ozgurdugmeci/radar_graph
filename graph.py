st.subheader('Graph')
df = pd.read_excel(yol,'graph')
fig = px.line_polar(df, r="points",
                    theta="categories",
                    color="player",
                    line_close=True,
                    color_discrete_sequence=["#00eb93", "#4ed2ff"],
                    template="plotly_dark" )

fig.update_polars(angularaxis_showgrid=False,
                  radialaxis_gridwidth=0,
                  gridshape='linear',
                  bgcolor="#494b5a",
                  radialaxis_showticklabels=False
                  )

fig.update_layout(paper_bgcolor="#494b5a",legend=dict(font=dict(size=12, color="white")))
fig.update_layout(font=dict(size=12, color="white"))

st.plotly_chart(fig)
