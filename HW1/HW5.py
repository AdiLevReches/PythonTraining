'''hw5'''
print("q1")

def Read_Lines_From_File(infile):
    with open(infile) as fileReader:
        lines = fileReader.read()
        return(lines)

def Write_Lines_To_File(lines, outfile):
    with open(outfile, 'w') as fileWriter:
        fileWriter.write(lines)

def copy_no_spaces(infile, outfile):
    lines = Read_Lines_From_File(infile)
    lines_witohut_spaces = lines.replace(" ","")
    Write_Lines_To_File(lines_witohut_spaces,outfile)

copy_no_spaces('infile.txt','outfile.txt')


print("q2")

def create_dict_freq(Candidate_List):
    Candidate_Dict = {}
    for candidate_key in Candidate_List:
        Candidate_Dict[candidate_key] = Candidate_Dict.get(candidate_key,0) + 1
    return(Candidate_Dict)

def num_max_candidate(Candidate_Dict):
    max_candidate = []
    most_votes = max(Candidate_Dict.values())
    for candidate_key in Candidate_Dict.keys():
        if Candidate_Dict[candidate_key]==most_votes:
            max_candidate.append(candidate_key)
    return(max_candidate)

def check_elections(votes):
    # if not all(isinstance(item, int) for item in votes):
    #     print("-1")
    for i in range(0,len(votes)):
        try:
            int(votes[i])
        except ValueError:
            print("-1")
            return
    print("1")
    dict = create_dict_freq(votes)
    print(num_max_candidate(dict))

check_elections([1,2,4,3,4,4,3,3])


'''q3'''
print("q3")
def get_csv_matrix(filename)
with open(infile) as fileReader:
    lines = fileReader.read()
