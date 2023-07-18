# ** Laporan Proyek Machine Learning - Tony Wijaya **

## Project Overview

### Latar Belakang
Pada bagian ini, Kamu perlu menuliskan latar belakang yang relevan dengan proyek yang diangkat.


## Business Understanding

Pada bagian ini, Anda perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Approach” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution approach (algoritma atau pendekatan sistem rekomendasi).

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai jumlah data, kondisi data, dan informasi mengenai data yang digunakan. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

_[Dataset](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset)_ yang digunakan berasal dari kaggle. _Dataset_ hanya berisi 1 data yaitu imdb_movies.csv yang berisi data movies dari _Internet_ _Movie_ _Database_ (IMDb) yang merupakan _database_ informasi online yang berkaitan dengan film, serial televisi, podcast, video rumahan, video game, dan konten streaming online – termasuk pemeran, kru produksi dan biografi pribadi, ringkasan plot, trivia, peringkat, dan ulasan penggemar dan kritis.

Berikut adalah variabel yang digunakan pada _dataset_ tersebut

* _names_ : Nama film. Variabel ini berisi nama-nama film dalam dataset. Setiap entri mewakili satu film.
* _date_x_ : Tanggal rilis film. Variabel ini menyimpan tanggal rilis setiap film dalam format tanggal.
* _score_ : Skor atau rating film. Variabel ini berisi skor atau rating yang diberikan kepada setiap film, mungkin berdasarkan penilaian kritikus, peringkat pengguna, atau metrik lainnya.
* _genre_ : Genre film. Variabel ini berisi informasi tentang genre-genre yang mendefinisikan kategori film tersebut, misalnya, drama, komedi, aksi, fiksi ilmiah, dsb.
* _overview_ : Ringkasan atau deskripsi singkat film. Variabel ini berisi ringkasan atau deskripsi singkat tentang plot atau isi dari setiap film.
* _crew_ : Informasi tentang kru produksi film. Variabel ini mungkin berisi nama-nama orang yang terlibat dalam produksi film, seperti sutradara, penulis skenario, produser, dan anggota kru lainnya.
* _status_ : Status film. Variabel ini menunjukkan status produksi film, misalnya _"Released"_ (Telah dirilis), _"In Production"_ (Sedang diproduksi) dan _"Post Production"_ (pasca produksi).
* _orig_lang_ : Bahasa asli film. Variabel ini berisi informasi tentang bahasa asli yang digunakan dalam film.
* _budget_x_ : Anggaran produksi film. Variabel ini menunjukkan perkiraan biaya produksi film dalam mata uang tertentu.
* _revenue_ : Pendapatan film. Variabel ini berisi informasi tentang total pendapatan yang dihasilkan oleh film, biasanya dalam mata uang tertentu.
* _country_  : Negara produksi film. Variabel ini berisi informasi tentang negara atau negara-negara di mana film diproduksi.

Setelah melewati masa pembersihan berikut adalah deskripsi dari masing-masing variabel yang dibagi menjadi data numerik dan kategorikal

describe variabel

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.


## Daftar Pustaka

[1] J. Devlin, M. W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” NAACL HLT 2019 - 2019 Conf. North Am. Chapter Assoc. Comput. Linguist. Hum. Lang. Technol. - Proc. Conf., vol. 1, no. Mlm, pp. 4171–4186, 2019.

[2] M. Fajriansyah, P. P. Adikara, and A. W. Widodo, “Sistem Rekomendasi Film Menggunakan Metode Content Based Filtering,” J. Pengemb. Teknol. Inf. dan Ilmu Komput., vol. 5, no. 6, pp. 2188–2199, 2021, [Online]. Available: http://e-journal.uajy.ac.id/20600/.

[3] E. Ryana Agustian and E. Prasetyo Nugroho, “Sistem Rekomendasi Film Menggunakan Metode Collaborative Filtering dan K-Nearest Neighbors Film Recommendation System Using Collaborative Filtering Method and K-Nearest Neighbors,” vol. 3, no. 1, pp. 18–21, 2020, [Online]. Available: https://ejournal.upi.edu/index.php/JATIKOM.