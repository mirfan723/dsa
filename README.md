# About Huffman Coding
Huffman coding is a compression algorithm that assigns variable-length codes to input symbols based on their frequency in the data. It constructs a binary tree where frequently occurring symbols have shorter codes. During compression, the tree is traversed to encode the input, reducing the overall bit representation. During decompression, the tree is used to decode the compressed data. This approach ensures efficient encoding and decoding, making Huffman coding widely used in various data compression applications.
# Project Working
The project is created using flask framework with html,css and javascript for the frontend. The logic for the huffman coding is written in python.
![image](https://github.com/mirfan723/dsa/assets/113796548/c4cfc7a5-19d5-42bf-96ab-dfaa3c8d4b6a)
# File Compression
In the compression process, when a user uploads a file, it is saved in the "uploads" directory. The compression.huffmancode class orchestrates the Huffman coding algorithm. First, it analyzes the frequency of each character in the input text, constructing a Huffman binary tree based on these frequencies. The text is then encoded using the generated Huffman codes, resulting in a compressed representation. To ensure a fixed byte size, the encoded text is padded, and information about the padding is prepended. The padded and encoded text is subsequently converted into a byte array. The final step involves writing this byte array to a binary file with a '.bin' extension in the "download" directory
![image](https://github.com/mirfan723/dsa/assets/113796548/f26d1a78-c270-41ca-a657-01bb6d0c400f)
# File Decompression
In the decompression phase, when a user uploads a compressed file, it is saved in the "uploads" directory. The compression.huffmancode class, responsible for both compression and decompression, is employed again. The decompression process begins by reading the compressed file and extracting the padded and encoded text. The Huffman tree, constructed during compression, is then used to decode the text back to its original form. The padding information is removed, resulting in the decompressed text. This text is saved in a new file with a '_decompressed.txt' extension in the "download" directory.
![image](https://github.com/mirfan723/dsa/assets/113796548/6d250a8b-daee-4850-929c-69bbbb84183f)
# File Compression and Decompression Examples
## Compressed File:
![image](https://github.com/mirfan723/dsa/assets/113796548/f4139816-5064-4e17-bda0-60efed162277)
![image](https://github.com/mirfan723/dsa/assets/113796548/d985d74f-0ede-4677-ad29-542a34cd1ae5)
### After Compression
![image](https://github.com/mirfan723/dsa/assets/113796548/28439e82-2b82-4811-b3ba-40f10248aadc)
## Decompressed File:
![image](https://github.com/mirfan723/dsa/assets/113796548/5c2eca11-9a30-4e07-a87e-4f48b8b2c51b)
![image](https://github.com/mirfan723/dsa/assets/113796548/d9b693b4-1163-4835-ba35-50a6093f9eb1)




