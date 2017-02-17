import pandas as pd

def organize_coasts():

    westcoast = ['california', 'oregon']
    eastcoast = ['maryland', 'new_york']


    df = pd.read_table("identified_samples.txt", sep=" ", header=None)
    print(df)
    
    #Give the columns names
    # You could also just use columns numbers, but I like to name my columns
    df.columns = ['ID', 'location']
    print(df)
    
    #Filter values.
    #Syntax is 'get rows where it's true that the value in 'location' is in the list westcoast'
    west_df = df[df['location'].isin(westcoast)]
    east_df = df[df['location'].isin(eastcoast)]

    west_df.to_csv('westcoast_samples.csv', index=False, header=False)
    east_df.to_csv('eastcoast_samples.csv', index=False, header=False)


if __name__ == "__main__":
    organize_coasts()


