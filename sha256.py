import hashlib
import time

def get_file_checksum(filename):
    with open(filename, 'rb') as f:
        hmm = f.read()
        sha256 = hashlib.sha256()
        sha256.update(hmm)
        return sha256.hexdigest()
    
filename = input("Masukkan Nama File :")

start_time = time.time()

checksum = get_file_checksum(filename)
print("Checksum (SHA-256): ", checksum)
end_time = time.time()
execution_time = end_time - start_time

print("Waktu eksekusi total: {:.9f} detik".format(execution_time))

