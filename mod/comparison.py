import os.path


class Comparison:
    def compare_tunes(self, tune1, tune2, dest, resultFile, comt1, comt2):
        tune1only = []
        tune2only = []
        both_change = []

        for i in range(len(tune1)):
            for b in range(len(tune2)):
                if tune2[b] == tune1[i]:
                    both_change.append(tune1[i])
                    break
            tune1only.append(tune1[i])

        for k in range(len(tune2)):
            if tune2[k] not in both_change:
                tune2only.append(tune2[k])

        fileLocationName = os.path.join(dest, resultFile+".txt")

        results = open(fileLocationName, "w+")
        results.write("******************************************\n")
        results.write("\n")
        results.write("BELOW ARE ADDRESSES CHANGED IN BOTH TUNES!\n")
        results.write("\n")
        results.write("******************************************\n")

        for r in range(len(both_change)):
            results.write(both_change[r]+"\n")

        results.write("*******************************************\n")
        results.write("\n")
        results.write("BELOW ARE ADDRESSES CHANGED ONLY IN TUNE 1!\n")
        results.write(comt1 + "\n")
        results.write("*******************************************\n")

        for x in range(len(tune1only)):
            results.write(tune1only[x]+"\n")

        results.write("*******************************************\n")
        results.write("\n")
        results.write("BELOW ARE ADDRESSES CHANGED ONLY IN TUNE 2!\n")
        results.write(comt2 + "\n")
        results.write("*******************************************\n")

        for j in range(len(tune2only)):
            print(tune2only[j])
            results.write(tune2only[j]+"\n")

        results.close()
