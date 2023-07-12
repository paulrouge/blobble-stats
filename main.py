from functions.funcs import getOwnwerOfBlobble, \
    getTotalAmountOfBlobbles, \
    getAllOwnersOfBlobbles

ownerPerBlobble = getAllOwnersOfBlobbles()

# iterate over all entries in the ownerPerBlobble dictionary
for blobbleId in ownerPerBlobble:
    print(f'Blobble {blobbleId} is owned by {ownerPerBlobble[blobbleId]}')
