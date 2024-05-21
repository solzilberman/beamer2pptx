## 📜 beamer2pptx
> Convert [beamer](https://ctan.org/pkg/beamer/?lang=en) presentations to powerpoints

### Install 
```bash
git clone repo-url beamer2pptx
cd beamer2pptx
pip3 install -r requirements.txt
```

### Usage
```bash
python3 main.py -i test.pdf -o test.pptx
```

#### Dependencies
- [pdftoppm](https://manpages.ubuntu.com/manpages/focal/en/man1/pdftoppm.1.html)


#### Limitations
- pdftoppm rasterizes each beamer slide as png. This results in worse quality slides. 