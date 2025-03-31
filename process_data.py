import pandas as pd

df = pd.read_csv("50_states.csv")
df.set_index("state", inplace=True)

def check_state(us_state_input):
    if us_state_input in df.index:
        state_info = df.loc[us_state_input]
        x = state_info["x"]
        y = state_info["y"]
        return x,y
    return 0,0
