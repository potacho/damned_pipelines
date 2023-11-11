import argparse

def filter_lab(df, lab_name):
    df = df[df["lab_name"] == lab_name]
    return df

def argument_parser():
    parser = argparse.ArgumentParser(description='Generate a table just for this particular lab.')
    help_message = "You have to select the lab"
    parser.add_argument("-l", "--lab", help=help_message, type=str)
    args = parser.parse_args()
    return args