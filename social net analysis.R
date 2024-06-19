#Social network Analysis

library(igraph) #igraph package
g <- graph(c(1,2,2,3,3,4,4,1), directed = F, n =8) #1 send mail to 2,2 sends mail to 3, 3 sends mail to 4....
plot(g, vertex.color="Pink", vertex.size = 50, edge.color="Blue")
g[]
g1 <- graph(c("yash", "Bhavya","Bhavya", "mehdi","mehdi","abhishek", "abhishek", "saranya", "saranya", "sasi","saranya","yash"))
plot(g1, vertex.color="orange",vertex.size= 50, edge.color="violet")

g1

#Network measures
degree(g1, , mode="all")
degree(g1, mode = "in")
degree(g1, mode = "out")
diameter(g1, directed=F, weights = NA)
edge_density(g1, loops = F)
ecount(g1)/(vcount(g1)*(vcount(g1)-1))
ecount(g1)
reciprocity(g1)
closeness(g1, mode="all", weights=NA)
betweenness(g1,directed=T, weights=NA)


data <-read.csv(file.choose(), header = T)
data
y <- data.frame(data$first, data$second)

net <- graph.data.frame(y, directed=T)
V(net)$label <- V(net)$name
V(net)$degree <- degree(net)

hist(V(net)$degree,
     col ="blue",
     main = "Histogram of Node Degree",
     ylab = "Frequency",
     xlab = "Degree of Vertices")
