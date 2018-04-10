import re

def parsers(URL):
    extension_string = " "
    extensions = ["3g2","3gp","7z","ai","apk","arc","arj","asp","aspx","avi","bak","bat","bin","bmp","c","cab","cfg","cfm","css","cgi","class","cer","com","cpp","cpl","cs","csv","cur","dat","deb","dll","dmp","doc","drv","exe","flv","fnt","fon","gadget","gif","gz","h","h264","htm","html","icns","ico","ini","jar","java","jpg","jpeg","js","jsp","key","lnk","m4v","mkv","mov","mp4","mpg","mpeg","msi","odp","ods","odt","otf","part","pdf","pds","php","pkg","pl","png","pps","ppt","pptx","ps","psd","psp","py","ra","rar","rm","rpm","rss","rtf","sh","sit","svg","swf","swift","sys","tar","tif","tiff","tmp","ttf","txt","vb","vob","wmv","wps","wpd","wsf","xhtml","xlr","xls","xlsx","xml","xz","z","zip"]
    res = URL.rpartition(".")[-1]
    res1 = URL.rpartition(".")[-3]
    res2 = res1.rpartition(".")[-1]

    if res2 in extensions:
        extension_string += "."
        extension_string += res2  #appends first extension if present
        if res in extensions:
            extension_string += "."
            extension_string += res  #appends second extension if present
    return(extension_string) #returns  full file extension needed

def main():
    url="https://www.torproject.org/dist/torbrowser/7.5.3/tor-browser-linux64-7.5.3_en-US.tar.xzhttps://www.torproject.org/dist/torbrowser/7.5.3/tor-browser-linux64-7.5.3_en-US.tar.xz"
    my_ext = parsers(url)
    sample_file = "my_code_file"
    print (sample_file+my_ext)

if __name__ == '__main__':
    main()

