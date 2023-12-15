#import necessary module and library
from flask import Flask,render_template,request,send_file,redirect
import os,glob,compression,shutil


global filename
global path
global file_name
app = Flask(__name__)
app.config["FILE_UPLOADS"]=os.path.abspath("")
# route to get the homepage
@app.route("/")
def index():
    filelist = glob.glob('uploads/*')
    filelist1=glob.glob('download/*')
    for f in filelist:
        os.remove(f)
    for f in filelist1:
        os.remove(f)

    return render_template('index.html')
# route to get the file and compress it 
@app.route("/compress",methods=['GET','POST'])
def compress():
    global filename
    global file_name
    if (request.method== 'GET'):
        return render_template("compress.html", check=0)
    else:
        up_file=request.files["file"]
        filename=up_file.filename;
        path=os.path.join(app.config["FILE_UPLOADS"],"uploads",filename)
        #calling of the module compression which contains the logic of compression and decompression of the file
        comp=compression.huffmancode(path)
        #if file is selected for upload
        if(len(up_file.filename)>0):
               #save the uploaded file
               up_file.save(os.path.join(app.config["FILE_UPLOADS"],"uploads",up_file.filename))
               #Perform compression and move the files to appropriate directories
               compressed_path=comp.compression()
               file_name=os.path.basename(compressed_path)
               shutil.move(os.path.join(app.config["FILE_UPLOADS"],"uploads", up_file.filename), os.path.join(app.config["FILE_UPLOADS"],"Temp", up_file.filename))
               shutil.move(os.path.join(app.config["FILE_UPLOADS"],"uploads", file_name), os.path.join(app.config["FILE_UPLOADS"],"download", file_name))
               file_upload = glob.glob("uploads/*")
               for f in file_upload:
                   os.remove(f)
               
               return render_template("compress.html",check=1);
        else:
            #if no file is selected for upload
            return render_template("compress.html",check=-1)
#route to decompress the file to its original state
@app.route("/decompress",methods=['GET','POST'])
def decompress():
     global file_name
     if(request.method=='GET'):
          return render_template("decompress.html",check=0)
     else:
        up_file=request.files["file"]
        #if file is selected for download
        if(len(up_file.filename)>0):
               up_file.save(os.path.join(app.config["FILE_UPLOADS"],"uploads",up_file.filename))
               filename1, file_extension = os.path.splitext(up_file.filename)
               
               filename1=filename1+".txt"
               
               path=os.path.join(app.config["FILE_UPLOADS"],"uploads",up_file.filename)
               comp=compression.huffmancode(os.path.join(app.config["FILE_UPLOADS"],"Temp",filename1))
               h= comp.compression()
               #perform decompression
               decompressed_path=comp.decompress(path)
               file_name=os.path.basename(decompressed_path)
              
               shutil.move(os.path.join(app.config["FILE_UPLOADS"],"uploads", file_name), os.path.join(app.config["FILE_UPLOADS"],"download", file_name))
               file_upload = glob.glob("uploads/*")
               for f in file_upload:
                   os.remove(f)
               return render_template("decompress.html",check=1) 
        else:
            #if no file is selected for download
            return render_template("decompress.html",check=-1)   

         
   

# route to handle file download
@app.route("/download")
def download():
    global filename
    global file_name
    path=os.path.join(app.config["FILE_UPLOADS"],"download",file_name)
    return send_file(path,as_attachment=True)
    
    
    
   
    
# Run the flask application
if __name__== "__main__":
   app.run(debug=True)
