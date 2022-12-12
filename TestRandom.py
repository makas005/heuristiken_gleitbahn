import IOptimizer
import Eval

height = 10
length = 10
n_nodes = 10
eval = Eval.Eval(height, length/(n_nodes+1))
opt = IOptimizer.IOptimizer(n_nodes, -height, height, eval.eval_func, "RandomSearch")

random_optimized = opt.Optimize()
eval.eval_func(random_optimized)
print(random_optimized)