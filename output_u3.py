import pandas as pd


def FED(file_path,spacing):
    Coord = pd.read_csv('COOR_BFAF.csv', sep='\s+')
    U = pd.read_csv(file_path,sep='\s+',nrows=3838)
    # Load the CSV file into a pandas DataFrame
    data_df = pd.concat([Coord,U],axis=1)
    data_df ['Z']=-data_df ['Z']
    # Filter out the data where Coor1 is equal to 2.8 or closest to 2.8
    # First, check if there is any data with Coor1 exactly equal to 2.8
    coor1_exact_match = data_df[abs(data_df['X'] - spacing)<0.02]

    if coor1_exact_match.empty:
        # If no exact match, find the data with Coor1 closest to 2.8
        closest_coor1 = data_df.iloc[(data_df['X'] - spacing).abs().argsort()[:1]]
    else:
        closest_coor1 = coor1_exact_match

    # Drop all other columns except Coor3 and U3
    filtered_data = closest_coor1[['Z', 'U3']]
    filtered_data =filtered_data.sort_values(by='Z')
    return filtered_data

y_matrix = FED('0u.csv',4.98)
#print(FED('U10.csv'))
#FED('U10.csv').to_csv('11.csv')
for i in range(1,83):
    y_matrix = pd.concat([y_matrix,FED(f'{i}u.csv',4.98)['U3']],axis=1)
    

y_matrix .to_csv('y_matrix_498.csv')


