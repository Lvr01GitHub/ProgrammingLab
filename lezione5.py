#Modificate l’oggetto CSVFile della lezione precedente in modo che dia un messaggio d’errore se si cerca di aprire un file non esistente.
#Poi, aggiungete questi due campi al file “shampoo_sales.csv”:
#01-01-2015,
#01-02-2015,ciao
#e gestite gli errori che verranno generati in modo che le linee vengano saltate ma che venga stampato a schermo l’errore


class CSVFile:
    
    def __init__(self,name):
        self.name = name

    def get_data(self):

        values = []

        try:
            my_file = open(self.name, "r")
        except Exception as e:
            print('Errore nella lettura del file: "{}"'.format(e))
            return None


        for line in my_file:

            elements = line.split(',')
            if elements[0] != 'Date':

                date = elements[0]
                value = elements[1]

                try:
                    value=float(value)
                except Exception as e:
                    print('Errore nela conversione a float: "{}"'.format(e))
                    continue
                values.append((value))
                
        my_file.close()

        return values


mio_file = CSVFile(name='shampoo_sales.csv')


print(mio_file.name)
print(mio_file.get_data())
