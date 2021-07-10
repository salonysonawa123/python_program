class my_dict:
    def __init__(self):
        self.data = {}

    def push(self,key,val):
        self.data[key]= val 
        return self.data

    def pop(self,key):
        if len(self.data)==0:
            print("Dictionary is Empty")
        elif key in self.data:
            return self.data.pop(key)
        else:
            print(f"{key} Is Not Present")

    def popitem(self):
        length = len(self.data)
        for i in self.data:
            x= self.data[i]
        for j in range(length):
            if j==length-1:
                return self.data.pop(i)
        return self.data

    def item(self):
        my_dict_x = []
        for i in self.data:
            x= self.data[i]
            #Dic_x= {i : x}                                      # Dic_x = (i,x)   --- original items output like .itmes() really work
            Dic_x = (i, x)
            my_dict_x.append(Dic_x)

        my_dict_x = f"Dict items ({my_dict_x})"
        print(my_dict_x)

    def keys(self):
        my_dict_x = []
        for i in self.data:
            my_dict_x.append(i)

        keys = f"Dict_Keys ({my_dict_x})"
        return keys

    def values(self):
        my_dict_x = []
        for i in self.data:
            x = self.data[i]
            my_dict_x.append(x)

        vals = f"Dict_Values ({my_dict_x})"
        return vals

a = my_dict()



#print(a.data)
#a.pop(9)
a.push('11','Elleven')
a.push(12,'Twellve')
print(a.data)
a.push(13,'Thirteen')
a.push(14,'Fourteen')
a.push(15,'Fifteen')
a.push(16,'Sixteen')
a.push(17,'Seventeen')

#print(a.data)

b  = a.popitem()
#print(b)
    
print(a.data)
a.item()
a.pop('11')
a.keys()
print(a.keys())
print(a.values())






