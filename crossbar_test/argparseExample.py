#  if __name__ == '__main__' :
# ApplicationRunner(
# url = 'wss://demo.crossbar.io/ws', # Même routeur que le composant JS
# realm = 'realm1', # Même namespace que le composant JS
# extra = {'msg' : 'Mouarfarfarf !'} # Paramètres passés au composant Python
# ).run(SexyComponent)


import argparse
import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments():
    parser = argparse.ArgumentParser() # argument erstellen
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""") # argument hinfügen,
    # welche parameters ist hier angenommen
    return parser.parse_args() # argument zurück geben

if __name__ == '__main__':
    args = parse_arguments()
    if args.extension == 'xml':
        x_an.launch_analysis('SyceronBrut.xml')
    elif args.extension == 'csv':
        c_an.launch_analysis('current_mps.csv')






# #! /usr/bin/env python3
# # coding: utf-8
# import argparse

# import analysis.csv as c_an
# import analysis.xml as x_an

# def parse_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
#     parser.add_argument("-d","--datafile",help="""CSV file containing pieces of information about the members of parliament""")
#     return parser.parse_args()

# def main():
#     args = parse_arguments()
#     datafile = args.datafile
#     if args.extension == 'xml':
#         x_an.launch_analysis(datafile)
#     elif args.extension == 'csv':
#         c_an.launch_analysis(datafile)

# if __name__ == "__main__":
#     main()




