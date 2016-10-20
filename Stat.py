class Stat:
    def __init__(self, chrom, transcript, strand, sample, start, end, length, total, mean, _min, q1, median, q3, _max, sem=None):
        self.chrom = chrom
        self.transcript = transcript
        self.strand = strand
        self.sample = sample
        self.start = int(start)
        self.end = int(end)
        self.length = round(float(length),2)
        self.total = round(float(total),2)
        self.mean = round(float(mean),2)
        self._min = round(float(_min),2)
        self.q1 = round(float(q1),2)
        self.median = round(float(median),2)
        self.q3 = round(float(q3),2)
        self._max = round(float(_max),2)
        try:
            self.sem = round(float(sem),2)
        except ValueError:
            self.sem = None

    def __str__(self):
        return ('\t').join([str(x) for x in [self.chrom, self.transcript, self.strand, self.sample, self.start, self.end, self.length, self.total, self.mean, self._min, self.q1, self.median, self.q3, self._max, self.sem]])

    def __repr__(self):
        return ('\t').join([str(x) for x in [self.chrom, self.transcript, self.strand, self.sample, self.start, self.end, self.length, self.total, self.mean, self._min, self.q1, self.median, self.q3, self._max, self.sem]])

    @staticmethod
    def parseStat(stat, header=True):
        results = []
        with open(stat, 'r') as f:
            if header:
                head = f.readline()
            for line in f:
                stat = Stat(*line.strip().split('\t'))
                results.append(stat)
        return results

    @staticmethod
    def groupStat(parsed):
        results = {}
        for stat in parsed:
            if stat.chrom not in results:
                results[stat.chrom] = {}
            if stat.transcript not in results[stat.chrom]:
                results[stat.chrom][stat.transcript] = []
            results[stat.chrom][stat.transcript].append(stat)
        for chrom in results:
            for gene in results[chrom]:
                results[chrom][gene] = sorted(results[chrom][gene], key=lambda x: x.start)
        return results
