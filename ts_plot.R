setwd('C:/Users/hafez/personal/r/oceanography')
library(marelac)
library(plot3D)
data<- read.csv('tsdata2008_2020.csv')

ts<-data[,3:4]

mint=min(ts['temperatureSurface'])
maxt=max(ts['temperatureSurface'])
mins=min(ts['salinitySurface'])
maxs=max(ts['salinitySurface'])


salC<-seq(from=mins,to=maxs,length.out = 156)
tempC<-seq(from=mint,to=maxt,length.out = 156)

sigma.c<-outer(salC,tempC,FUN = function(S,t)sw_dens(S = S, t = t)-1000)
sigma.c

png(file = 'ts_diagram.png',width = 15,res=500,pointsize = 12,bg='white')


jpeg(file="ts_diagram.jpeg")
par(mar=c(5,5,4,6))
contour2D(x=salC,y=tempC,z=sigma.c,lwd=2,main='General T-S (Temperature and salinity) Diagram',
          col='black',xlab=expression('Sanlinity(???)'),ylab=expression('Temperature("~degree*C")'))
temp<-unlist(ts['temperatureSurface'],use.names = FALSE)
sal<-unlist(ts['salinitySurface'],use.names = FALSE)
sigma_theta<-sw_dens(S=sal,t=temp)-1000
scatter2D(sal,temp,colvar = sigma_theta,pch=16,cex=1.25,add=TRUE,
          clim = range(sigma.c),colkey = FALSE)
colkey(clim = range(sigma.c),dist = 0.005,side=4,add=TRUE,
       clab = expression('Density(kg m"^-3")'),col.clab = 'black',
       side.clab = 4,line.clab = 2.5,length = 1,width = 0.8,
       col.axis = 'black',col.ticks = 'black',cex.axis = 0.9)

dev.off()









