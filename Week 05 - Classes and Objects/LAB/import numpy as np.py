import numpy as np
import pandas as pd
from lets_plot import *

LetsPlot.setup_html()

# Create a random number generator
rng = np.random.default_rng()

# Generate 1000 samples, each containing 10 dice rolls
rolls = rng.integers(1, 7, size=(1000, 10))

# Calculate the mean of each sample
sample_means = rolls.mean(axis=1)

# Display the sample means
print(sample_means)

# Calculate the statistics
print("Mean:", sample_means.mean())
print("Standard deviation:", sample_means.std())
print("Minimum:", sample_means.min())
print("Maximum:", sample_means.max())

# Calculate the quantiles
print("0.025 quantile:", np.quantile(sample_means, 0.025))
print("0.975 quantile:", np.quantile(sample_means, 0.975))

# Convert the array into a dataframe
dataframe = pd.DataFrame({"x": sample_means})

# Plot a histogram
(
    ggplot(data=dataframe) +
    geom_histogram(aes(x="x", y="..density.."), bins=15) +
    labs(
        title="Sampling Distribution of the Sample Mean (n=10)",
        x="Sample Mean",
        y="Density"
    )
)