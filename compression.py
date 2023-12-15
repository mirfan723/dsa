import heapq,os

# Define a BinaryTree class for Huffman coding
class BinaryTree:
    def __init__(self,value,frequ):
        self.value = value
        self.frequ = frequ
        self.left =None
        self.right = None

    def __lt__(self,other):
        print("hello");
        return self.frequ < other.frequ

    def _eq_(self,other):
        return self.frequ == other.frequ
# Define a HuffmanCode class to perform compression and decompression
class huffmancode:

    def __init__(self,path):
                self.path=path
                self.__heap = []
                self.__code = {}
                self.__reversecode = {}
    def __frequency_from_text(self,text):
        # Calculate frequency of each character in the text
        frequ_dict={}
        for char in text:
            if char not in frequ_dict:
                frequ_dict[char]=0
            frequ_dict[char] += 1
        return frequ_dict


    def __Build_heap(self,frequency_dict):
         # Build a min heap for characters based on their frequencies
        for key in frequency_dict:
            frequency = frequency_dict[key]
            binary_tree_node = BinaryTree(key,frequency)
            heapq.heappush(self.__heap , binary_tree_node)

    def __Build_Binary_Tree(self):
        # Build a Huffman binary tree from the min heap
        while len(self.__heap) > 1:
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heapq.heappop(self.__heap)
            sum_of_freq = binary_tree_node_1.frequ + binary_tree_node_2.frequ
            newnode = BinaryTree(None,sum_of_freq)
            newnode.left = binary_tree_node_1
            newnode.right = binary_tree_node_2
            heapq.heappush(self.__heap,newnode)
        return

    def __Build_Tree_Code_Helper(self,root,curr_bits):
          # Recursively build Huffman codes and reverse codes
        if root is None:

            return
        if root.value is not None:
            print("working")
            self.__code[root.value] = curr_bits
            self.__reversecode[curr_bits] = root.value
            return
        self.__Build_Tree_Code_Helper(root.left,curr_bits+'0')
        self.__Build_Tree_Code_Helper(root.right,curr_bits+'1')

    def __Build_Tree_Code(self):
           # Build Huffman codes and reverse codes from the Huffman tree
        root = heapq.heappop(self.__heap)
        self.__Build_Tree_Code_Helper(root,'')

    def __Build_Encoded_Text(self,text):
          # Encode the input text 
        encoded_text = ''
        for char in text:
            encoded_text += self.__code[char]
        return encoded_text

    def __Build_Padded_Text(self,encoded_text):
         # Pad the encoded text to make its length a multiple of 8
        padding_value = 8 -len(encoded_text) % 8
        for i in range(padding_value):
            encoded_text += '0'
        padded_info = "{0:08b}".format(padding_value)
        padded_text= padded_info + encoded_text
        return padded_text

    def __Build_Bite_Array(self,padded_text):
        # Convert the padded text into a byte array
        array = []
        for i in range(0,len(padded_text),8):
            byte = padded_text[i:i+8]
            array.append(int(byte,2))
        return array

    def compression(self):
         # Compress the file and return the path of the compressed file
        
        print("Compression has Started")
        filename,file_extension = os.path.splitext(self.path)
        output_path = filename + '.bin'
        with open(self.path,'r+') as file ,open(output_path,'wb') as output:
            text = file.read()
            text = text.rstrip()
            frequency_dict = self.__frequency_from_text(text)
            #Calculate frequency of each text and store it in freq. dict
            build_heap = self.__Build_heap(frequency_dict)
            #min heap for two minimum frequency
            #construct binary tree
            self.__Build_Binary_Tree()
            #construct code from binary tree and store it in dict
            self.__Build_Tree_Code()
#construct encoded text
            encoded_text = self.__Build_Encoded_Text(text)
#padding of encoded text
            padded_text = self.__Build_Padded_Text(encoded_text)
            bytes_array = self.__Build_Bite_Array(padded_text)
            final_bytes= bytes(bytes_array)
            output.write(final_bytes)
        print('Compressed Successfully')
        return output_path
        

    def __Remove_Padding(self,text):
         # Remove padding information from the text
        padded_info =text[:8]
        if len(padded_info) != 8:
            raise ValueError("Invalid padded_info length")
        padding_value =int(padded_info,2)
        text = text[8:]
        text = text[:-padding_value]
        print("hello")
        return text

    def __Decoded_Text(self,text):
        current_bits =''
        decoded_text = ''
        for char in text:
            current_bits +=char
            if current_bits in self.__reversecode:
                decoded_text += self.__reversecode[current_bits]
                current_bits = ''
        print("hello")        
        return decoded_text

    def decompress(self,input_path):
        # Decompress the file and return the path of the decompressed file
        print("Decompression Started")
        filename, file_extension = os.path.splitext(input_path)
        output_path = filename +'_decompressed'+ '.txt'
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ''
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)
            text_after_padding = self.__Remove_Padding(bit_string)
            actual_text = self.__Decoded_Text(text_after_padding)
            output.write(actual_text)
            print("Decompressed Successfully")
        return output_path


