import angr
import claripy

target = angr.Project('./fairlight', load_options={"auto_load_libs": False})
inp = claripy.BVS("inp", 0xe * 8)
entry_state = target.factory.entry_state(args=["./fairlight", inp])
simulation = target.factory.simulation_manager(entry_state)
simulation.explore(find = 0x401a6e, avoid = 0x040074d)
solution = simulation.found[0]
print(solution.solver.eval(inp, cast_to=bytes))
