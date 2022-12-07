import threading import time
def numPar(n ):
time_ini = time . time () i = 0 cont = 0
print ("Los n meros pares son : ") for i in range (n ): i f i % 2 == 0: print ( i )
cont += 1
	print ("Hay" ,cont ," n meros	pares ")
time . sleep (1) time_end = time . time ()
total = time_end − time_ini print ("El tiempo de e j e c u c i n es :" , total )
i f _name_ == ’_main_’ : thread = threading . Thread( target=numPar, args= (20 , )) thread . start () thread . join ()
