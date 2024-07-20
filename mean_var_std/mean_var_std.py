import numpy

def calculate(nums):
    count = 0
    
    if (len(nums)!=9):
        raise ValueError("List must contain nine numbers.")
    
    mat = numpy.array(nums).reshape(3,3)

    flat = mat.flatten()

    res = {}
    
    mean1=[numpy.mean(mat, axis=0).tolist(), numpy.mean(mat, axis=1).tolist(), numpy.mean(flat).tolist()]
    var1=[numpy.var(mat, axis=0).tolist(), numpy.var(mat, axis=1).tolist(), numpy.var(flat).tolist()]
    std_dev1=[numpy.std(mat, axis=0).tolist(), numpy.std(mat, axis=1).tolist(), numpy.std(flat).tolist()]
    max1=[numpy.max(mat, axis=0).tolist(), numpy.max(mat, axis=1).tolist(), numpy.max(flat).tolist()]
    min1=[numpy.min(mat, axis=0).tolist(), numpy.min(mat, axis=1).tolist(), numpy.min(flat).tolist()]
    sum1=[numpy.sum(mat, axis=0).tolist(), numpy.sum(mat, axis=1).tolist(), numpy.sum(flat).tolist()]

    res["mean"] = mean1
    res["variance"] = var1
    res["standard deviation"] = std_dev1
    res["max"] = max1
    res["min"] = min1
    res["sum"] = sum1

    return res