def find_closest_nft_values(nft_values, budget):
    left = 0
    right = len(nft_values) - 1

    if not nft_values:
        return (None,None)
        
    
    while left<=right:
        mid = (left+right)//2
        midValue = nft_values[mid]
        
        if midValue == budget:
            return(midValue,midValue)
        elif midValue < budget:
            lower = midValue
            left = mid +1 
        else:
            upperValue = midValue
            right = mid - 1

    return (lower,upperValue)



nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))