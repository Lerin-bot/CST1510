'Lets_plot''
from lets_plot import *
LetsPlot.setup_html()

(
    ggplot(data=penguins, mapping=aes(x="species"))
    + geom_bar()  
    + labs(
        title="Number of Penguins by Species",
        x="Penguin Species",
        y="Count"
    )
)
