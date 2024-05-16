import pandas as pd





def dollar_bar_creator(df_,asset,dollar_amt):

    #df_ = pd.read_csv(f'updated_data/train_data/pulled/{asset}_joined.csv')
 #   df_.sort_values(df_.index, inplace =True)
    
    close = 'Close'
    volume = 'Volume'
    
   


    vol_count = 0
    dollar_count = 0
    new_bar = []

    for i, d in df_.iterrows():


        dollar_count+=round((d[volume] * d[close]),2)
        #vol_count += d[volume]

        if dollar_count >= dollar_amt:
            bar ={'Date':i,'Close':d[close]}
            new_bar.append(bar)
         #   vol_count = 0 
            dollar_count = 0
         
        


        
        #print(dollar_count)
        #print(i,d)

    new_bar_df = pd.DataFrame(new_bar)
    new_bar_df['Returns'] = new_bar_df['Close'].pct_change()
    new_bar_df['Returns_100'] = new_bar_df['Returns'] *100


    return new_bar_df


def security_append(main_df, security_list):
    for asset_ in security_list:
        df_ = pd.read_csv(f'updated_data/{asset_}_1.csv')
        df_.sort_values('Date', inplace=True)
        df_ = df_.set_index('Date')
        df_ = df_[['Close', 'Volume']]

        # Join the dataframe with the main dataframe
        main_df = main_df.join(df_, how='left', rsuffix=f'_{asset_}')

    return main_df

    
    






    #return new_bar

'''
if __name__ in "__main__":

    df = pd.read_csv('updated_data/EURUSD.csv')

    print(df.head())

    print(dollar_bar_creator(df))
'''