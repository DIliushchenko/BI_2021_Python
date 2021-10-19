def gc_check(fast_seq, gc_bound):
    c = fast_seq.count('C')
    g = fast_seq.count('G')
    gc_sum = g + c
    nuc_len = len(fast_seq)
    gc_cont = (gc_sum / float(nuc_len)) * 100
    if gc_bound[0] <= gc_cont <= gc_bound[1]:
        return True
    else:
        return False


def length_check(length_seq, length_bound):
    if length_bound[0] <= length_seq <= length_bound[1]:
        return True
    else:
        return False


def quality_check(quality_seq, quality_threshold):
    score = 0
    for sym in quality_seq:
        score += (ord(sym) - 33)
    mean_score = score / len(quality_seq)
    if mean_score < quality_threshold:
        return False
    elif mean_score >= quality_threshold:
        return True


def cat_fasta(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold,
              save_filtered):
    with open(input_fastq, 'r') as input_file:
        correct_reads = open(output_file_prefix + '_passed.fastq', 'w')
        if save_filtered == True:
            failed_reads = open(output_file_prefix + '_failed.fastq', 'w')
        n = 0
        name_of_read = ''
        seq = ''
        ad = ''
        quality_line = ''
        for line in input_file:
            n += 1
            if n == 1:
                name_of_read = line
                len_seq = int(name_of_read.split(' ')[2].split('=')[1])
            if n == 2:
                seq = line
            if n == 3:
                ad = line
            if n == 4:
                quality_line = line
                test_gc = gc_check(seq, gc_bounds)
                test_len = length_check(len_seq, length_bounds)
                test_quality = quality_check(quality_line, quality_threshold)
                if test_gc == True and test_len == True and test_quality == True:
                    correct_reads.writelines([name_of_read, seq, ad, quality_line])
                else:
                    if save_filtered == True:
                        failed_reads.writelines([name_of_read, seq, ad, quality_line])
                n = 0  # go to the next read

        correct_reads.close()
        if save_filtered == True:
            failed_reads.close()


# Input data for program
print('Hello! This program created special for trimming reads by length, quality and gc content. Enjoy!\nIf you want '
      'default options just enter nothing')
input_fastq = input('Enter path of your reads including name of file in fastq format: ')
output_file_prefix = input('Enter path where you want to save your reads')
gc_input = input('Enter bounds for gc content (default = 0, 100), separated by spaces: ')
if gc_input == '':
    gc_bounds = 0, 100
elif len(gc_input.split(' ')) == 1:
    gc_bounds = 0, gc_input
elif len(gc_input.split(' ')) == 1:
    gc_bounds = (tuple(map(int, gc_input.split(' '))))

length_input = input('Enter bounds for length of read (default = 0, 2 ** 32), separated by spaces: ')
if length_input == '':
    length_bounds = 0, 2 ** 32
elif len(length_input.split(' ')) == 1:
    length_bounds = 0, length_input
elif len(length_input.split(' ')) == 1:
    length_bounds = (tuple(map(int, length_input.split(' '))))

quality_input = input('Enter threshold for quality of read (default = 0), enter just one number: ')
if quality_input == '':
    quality_threshold = 0
else:
    quality_threshold == int(uality_input)
save_filtered = input('Do you want to save failed reads? True or False required (def False): ')
if save_filtered == '':
    save_filtered = False
elif save_filtered == 'True':
    save_filtered = True
elif save_filtered == 'False':
    save_filtered = False

cat_fasta(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered)