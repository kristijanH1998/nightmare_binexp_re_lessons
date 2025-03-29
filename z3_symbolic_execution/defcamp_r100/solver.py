import angr

target = angr.Project('r100')
desired_adr = 0x4007a1
wrong_adr = 0x400790
entry_state = target.factory.entry_state(args=["./fairlight"])
simulation = target.factory.simulation_manager(entry_state)
simulation.explore(find = desired_adr, avoid = wrong_adr)
solution = simulation.found[0].posix.dumps(0)
print(solution)
