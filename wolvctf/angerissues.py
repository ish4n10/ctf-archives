

import angr
import claripy


success_addr = 0x40439F
failure_addr = 0x4011B1

print("Success address: ", hex(success_addr))
print("Failure address: ", hex(failure_addr))

binary = "./original"
proj = angr.Project(binary)


input_size = 60
flag_chars = [claripy.BVS(f'flag_{i}', 8) for i in range(input_size)]
flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n', 8)])  

state=proj.factory.entry_state(stdin=flag)

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=success_addr, avoid=failure_addr)

if simgr.found:
    solution_state = simgr.found[0]
    solution = solution_state.solver.eval(flag, cast_to=bytes)
    print(solution.decode().strip())
else:
    print("no solution exist")

