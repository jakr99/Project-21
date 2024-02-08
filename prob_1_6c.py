from automata.fa.dfa import DFA

prob_1_6c = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': 'q0', '0': 'q1'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'1': 'q0', '0': 'q3'},
        'q3': {'0': 'q1', '1': 'q4'},
        'q4': {'1': 'q4', '0': 'q4'}
    },
    initial_state='q0',
    final_states={'q4'}
)


