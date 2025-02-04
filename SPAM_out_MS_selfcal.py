# Selfcal of SPAM output MSs in CASA, which subsequently imaged in WSClean
# Change solint or minsnr parameters for better results
# Selfcal of 20sep data


def flagresidual(myfile):
        default(flagdata)
        flagdata(vis=myfile, mode ='rflag', datacolumn="RESIDUAL_DATA", field='', timecutoff=6.0,  freqcutoff=6.0,
                timefit="line", freqfit="line",        flagdimension="freqtime", extendflags=False, timedevscale=6.0,
                freqdevscale=6.0, spectralmax=500.0, extendpols=False, growaround=False, flagneartime=False,
                flagnearfreq=False, action="apply", flagbackup=True, overwrite=True, writeflags=True)
                

def mygaincal_ap(myfile,myref,mysolint,srno):
        if os.path.isdir('selfcal'+str(srno)+'.GT'):
                os.system('rm -rf '+'selfcal'+str(srno)+'.GT')
        default(gaincal)
        gaincal(vis=myfile, caltable='selfcal'+str(srno)+'.GT', append=False, field='0',
                solint = mysolint, refant = myref, minsnr = 2.0,solmode='L1R', gaintype = 'G',
                solnorm= False, calmode = 'p')
        mycal = 'selfcal'+str(srno)+'.GT'
        return mycal
        

def myapplycal(myfile,mycal):
        default(applycal)
        applycal(vis=myfile, field='0', gaintable=mycal, gainfield=['0'], applymode='calflag', 
                 interp=['linear'], calwt=False, parang=False)
        print('Ran applycal.')
        # correct the data weights
        statwt(vis=myfile, datacolumn='corrected')

#########################################################################
myfile = 'part1.ms'
myref = '0'
mysolint = '60s'
srno=1

flagresidual(myfile)

mycal=mygaincal_ap(myfile,myref,mysolint,srno)

myapplycal(myfile,mycal)

#########
myfile = 'part2.ms'
myref = '0'
mysolint = '60s'
srno=2

flagresidual(myfile)

mycal=mygaincal_ap(myfile,myref,mysolint,srno)

myapplycal(myfile,mycal)

###########
myfile = 'part3.ms'
myref = '0'
mysolint = '60s'
srno=3

flagresidual(myfile)

mycal=mygaincal_ap(myfile,myref,mysolint,srno)

myapplycal(myfile,mycal)

#######
myfile = 'part4.ms'
myref = '0'
mysolint = '60s'
srno=4

flagresidual(myfile)

mycal=mygaincal_ap(myfile,myref,mysolint,srno)

myapplycal(myfile,mycal)

#######
myfile = 'part5.ms'
myref = '0'
mysolint = '60s'
srno=5

flagresidual(myfile)

mycal=mygaincal_ap(myfile,myref,mysolint,srno)

myapplycal(myfile,mycal)

########
myfile = 'part6.ms'
myref = '0'
mysolint = '60s'
srno=6

flagresidual(myfile)

mycal=mygaincal_ap(myfile,myref,mysolint,srno)

myapplycal(myfile,mycal)





