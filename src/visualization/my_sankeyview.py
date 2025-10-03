# Honey child, let's flow these diagrams smoother than molasses on a hot summer day!
# ImportError: cannot import name 'gcd' from 'fractions'
import sankeyview as sv

nodes = ["Start", "Step1", "Step2", "End"]
links = [("Start", "Step1", 10), ("Step1", "Step2", 7), ("Step2", "End", 5)]

spec = sv.Spec(nodes=nodes, links=links)
diagram = sv.render(spec)
diagram.show()
