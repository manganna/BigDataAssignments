def main():
    
    total_pointList = 50000
    
    dim = 2
    
    num_clusters = 4
    
    cutoff = 0.5
    lat = []
    long = []
    pointList =[]
    for i in range(df.shape[0]):
        lat.append(df.values[i][1])
        long.append(df.values[i][2])
    pointListds = []
    for i in range(len(lat)):
        pointListds.append([float(lat[i]),float(long[i])])
    for i in pointListds:
        pointList.append(Point(i))

    clusters = kmeans(pointList, num_clusters, cutoff)

    '''
    for i,c in enumerate(clusters):
        for p in c.pointList:
            print (" Cluster: ", i, "\t Point :", p)
    '''
    if dim == 2 and PLOTLY_USERNAME:
        print ("Plotting pointList, launching browser ...")
        plotData(clusters)

class Point:
    '''
    An point in n dimensional space
    '''
    def __init__(self, coordinates):
        '''
        coordinates - A list of values, one per dimension
        '''
        
        self.coordinates = coordinates
        self.n = len(coordinates)
        
    def __repr__(self):
        return str(self.coordinates)

class Cluster:
    '''
    A set of pointList and their centroid
    '''
    
    def __init__(self, pointList):
        '''
        pointList - A list of point objects
        '''
        
        if len(pointList) == 0: raise Exception("ILLEGAL: empty cluster")
        # The pointList that belong to this cluster
        self.pointList = pointList
        
        # The dimensionality of the pointList in this cluster
        self.n = pointList[0].n
        
        # Assert that all pointList are of the same dimensionality
        for i in pointList:
            if i.n != self.n: raise Exception("ILLEGAL: wrong dim")
            
        # Set up the initial centroid (this is usually based off one point)
        self.centroid = self.calCentroid()
        
    def __repr__(self):
        '''
        String representation of this object
        '''
        return str(self.pointList)
    
    def iterativeUpdate(self, pointList):
        '''
        Returns the distance between the previous centroid and the new after
        recalculating and storing the new centroid.
        '''
        prev_centroid = self.centroid
        self.pointList = pointList
        self.centroid = self.calCentroid()
        displacement = fetchDis(prev_centroid, self.centroid) 
        return displacement
    
    def calCentroid(self):
        numpointList = len(self.pointList)
        coordinates = [p.coordinates for p in self.pointList]
        unz = zip(*coordinates)
        centroid_coord = [math.fsum(iList)/numpointList for iList in unz]
        
        return Point(centroid_coord)

def kmeans(pointList, k, cutoff):
    
    initial = random.sample(pointList, k)
    
    clusters = [Cluster([p]) for p in initial]
    
    loopCounter = 0
    while True:
        lists = [ [] for c in clusters]
        clusterCount = len(clusters)
        
        loopCounter += 1
        for p in pointList:
            smallest_distance = fetchDis(p, clusters[0].centroid)
            clusterIndex = 0
        
            for i in range(clusterCount - 1):
                distance = fetchDis(p, clusters[i+1].centroid)
                if distance < smallest_distance:
                    smallest_distance = distance
                    clusterIndex = i+1
            lists[clusterIndex].append(p)
        
        biggest_displacement = 0.0
        
        for i in range(clusterCount):
            displacement = clusters[i].iterativeUpdate(lists[i])
            biggest_displacement = max(biggest_displacement, displacement)
        
        if biggest_displacement < cutoff:
            print ("Program over after %s iterations" % loopCounter)
            break
    return clusters

def fetchDis(first, second):
    '''
    '''
    if first.n != second.n:
        raise Exception("Can't compare it.")
    
    ret = reduce(lambda x,y: x + pow((first.coordinates[y]-second.coordinates[y]), 2),range(first.n),0.0)
    return math.sqrt(ret)

def plotData(data):
    symbols = ['circle', 'cross', 'triangle-up', 'square']

    traceList = []
    for i, c in enumerate(data):
        data = []
        for p in c.pointList:
            data.append(p.coordinates)
        # Data
        trace = {}
        trace['x'], trace['y'] = zip(*data)
        trace['marker'] = {}
        trace['marker']['symbol'] = symbols[i]
        trace['name'] = "Cluster " + str(i)
        traceList.append(trace)
        # Centroid (A trace of length 1)
        centroid = {}
        centroid['x'] = [c.centroid.coordinates[0]]
        centroid['y'] = [c.centroid.coordinates[1]]
        centroid['marker'] = {}
        centroid['marker']['symbol'] = symbols[i]
        centroid['marker']['color'] = 'rgb(200,10,10)'
        centroid['name'] = "Centroid " + str(i)
        traceList.append( Scatter(centroid))

    # Style the chart
    layout = dict(title = 'Plot',
              xaxis = dict(title = 'X axis'),
              yaxis = dict(title = 'Y axis'),
        plot_bgcolor='lightblue',
              )

    fig = dict(data=traceList, layout=layout)
    iplot(fig)

if __name__ == "__main__": 
    main()