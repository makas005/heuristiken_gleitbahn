import IOptimizer
import Eval

height = 10
length = 10
n_nodes = 10
eval = Eval.Eval(height, length/(n_nodes+1))
opt = IOptimizer.IOptimizer(n_nodes, -height, height, eval.eval_func, "RasterSuche")

raster_optimized = opt.Optimize()
opt_value = eval.eval_func(raster_optimized)
print("Time:")
print(opt_value)
print("Vector:")
print(raster_optimized)