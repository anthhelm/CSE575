import csv


#combine dicts

def combine(int_dict,names_dict,writer):
    i=1
    for each in int_dict.keys():
        if each in names_dict:
            writer.writerow([int_dict[each],names_dict[each]])
            i+=1
    print i



if __name__ == "__main__":
    
    movies_writer = csv.writer(open('final_movies_dict.csv', 'wb'))
    users_writer = csv.writer(open('final_users_dict.csv', 'wb'))

    #Read user_int dict
    reader1 = csv.reader(open('users_int.csv', 'rb'))
    users_int = dict(x for x in reader1)

    #Read item_int dict
    reader2 = csv.reader(open('user_names.csv', 'rb'))
    user_names = dict(x for x in reader2)

    #Combine dictionaries {userid:user_int_id} and {userid:user_name}   
    combine(users_int,user_names,users_writer)

    #Read user_names dict
    reader3 = csv.reader(open('items_int.csv', 'rb'))
    items_int = dict(x for x in reader3)

    #Read movie_names dict
    reader4 = csv.reader(open('movie_names.csv', 'rb'))
    movie_names = dict(x for x in reader4)
    
    #Combine dictionaries {userid:user_int_id} and {userid:user_name} 
    combine(items_int,movie_names,movies_writer)
