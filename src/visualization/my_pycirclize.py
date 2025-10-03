# Well ain't this sweeter than sweet tea! Let's make some fancy circular plots, y'all!
from pycirclize import Circos

# Create circos plot with sectors (dictionary format: name -> size)
sectors = {"A": 10, "B": 20, "C": 30}
circos = Circos(sectors, space=5)

# Add text labels for each sector
for sector in circos.sectors:
    sector.text(sector.name, r=90, size=12)

# Save the plot
circos.savefig("circos_plot.png")
print("Basic circos plot saved as circos_plot.png")
