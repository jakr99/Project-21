from automata.fa.dfa import DFA

prob_1_6m = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1', ''},
    transitions={
        'q0': {'1': 'q0', '0': 'q0', '': 'q0'}, 
        'q1': {'0': 'q0', '1': 'q0', '': 'q0'},
        },
    initial_state='q0',
    final_states={'q1'}
)

