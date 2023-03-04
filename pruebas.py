from pymoo.problems import get_problem
from pymoo.util.plotting import plot

problem = get_problem("zdt3")
plot(problem.pareto_front(), no_fill=True)
