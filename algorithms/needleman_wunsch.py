def nw_align(seq1_fasta, seq2_fasta):
    def read_fasta(file_path):
        with open(file_path) as f:
            return ''.join(line.strip() for line in f if not line.startswith('>'))

    seq1 = read_fasta(seq1_fasta)
    seq2 = read_fasta(seq2_fasta)

    m, n = len(seq1), len(seq2)
    
    match, mismatch, gap = 1, -1, -2  # Make sure the gap penalty is consistent
    
    # Initialize the matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the first row and column
    for i in range(m + 1):
        dp[i][0] = i * gap
    for j in range(n + 1):
        dp[0][j] = j * gap
    
    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = max(dp[i-1][j-1] + match, dp[i-1][j] + gap, dp[i][j-1] + gap)
            else:
                dp[i][j] = max(dp[i-1][j-1] + mismatch, dp[i-1][j] + gap, dp[i][j-1] + gap)
    
    # Traceback
    i, j = m, n
    seq1_align, seq2_align = "", ""
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and ((seq1[i-1] == seq2[j-1] and dp[i][j] == dp[i-1][j-1] + match) or
                                (seq1[i-1] != seq2[j-1] and dp[i][j] == dp[i-1][j-1] + mismatch)):
            seq1_align = seq1[i-1] + seq1_align
            seq2_align = seq2[j-1] + seq2_align
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + gap:
            seq1_align = seq1[i-1] + seq1_align
            seq2_align = "-" + seq2_align
            i -= 1
        else:
            seq1_align = "-" + seq1_align
            seq2_align = seq2[j-1] + seq2_align
            j -= 1
    
    # Generate match string
    match_string = ''.join('|' if a == b else '*' if a != '-' and b != '-' else ' ' for a, b in zip(seq1_align, seq2_align))
    
    # Calculate alignment score
    alignment_score = dp[m][n]  # Use the value in the bottom-right cell of the DP table
    
    return seq1_align, match_string, seq2_align, alignment_score
