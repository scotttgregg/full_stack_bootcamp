# peaks_and_valleys.py

data = [1, 2, 3, 4,	5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peaks = []
    for i in range(len(data)-1):
        if data[i - 1] < data[i] and data[i + 1] < data[i]:
            peaks.append(i)
    print(peaks)


def valleys(data):
    valleys = []
    for i in range(1, len(data)-1):
        if data[i - 1] > data[i] and data[i + 1] > data[i]:
            valleys.append(i)
    print(valleys)


def peaks_and_valleys(data):
    p_and_v = []
    for i in range(1, len(data)-1):
        if data[i - 1] < data[i] and data[i + 1] < data[i]:
            p_and_v.append(i)
        elif data[i - 1] > data[i] and data[i + 1] > data[i]:
            p_and_v.append(i)
    print(p_and_v)


peaks(data)
valleys(data)
peaks_and_valleys(data)