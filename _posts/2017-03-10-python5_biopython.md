---
layout: post
title: "Python V: Sequence Analysis with Biopython"
instructor: Claire
permalink: /python5_biopython/
materials: files/python6.zip
---

Biopython is a tour-de-force Python library which contains a variety of modules for analyzing and manipulating biological data in Python. While this library has lots of functionality, it is primarily useful for dealing with sequence data and querying online databases (such as NCBI or UniProt or the Protein Data Bank) to obtain information about sequences.
This [online tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html) describes nearly all the capabilities (with examples!) of things to do with Biopython (`ctrl+F` is your friend here!). 

## Download and install

You may need to download and install Biopython on your system. Instructions for this step are available [here]({{ site.baseurl }}{{ post.url }}/files/install_biopython.pdf).


## Reading and parsing sequence files

Biopython is an ideal tool for reading and writing sequence data. Biopython has two main modules for this purpose: `SeqIO` (sequence input-output) and `AlignIO` (multiple sequence alignment input-output). Each of these modules has two primary (although there are others!) functions: `read` and `parse`. The `read` function will read in a file with a single sequence or alignment, and the `parse` function will read in a file with multiple sequences or multiple sequence alignments. Each function takes two arguments: the file name and the sequence format (e.g. fasta, phylip, etc.)

<br>
Biopython parses sequence files into Biopython data structures, known as `SeqRecord` objects. Each sequence has several attributes (which you can examine with `dir()`), but the most important ones are `.seq`, `.id`, and `.description`.


{% highlight python %}
>>> from Bio import SeqIO

>>> records =  list(SeqIO.parse("seqs.fasta", "fasta")):
>>> print(records)

[SeqRecord(seq=Seq('AGCTAGATCGATGC', SingleLetterAlphabet()), id='1', name='1', description='1', dbxrefs=[]), SeqRecord(seq=Seq('ATCGATACA', SingleLetterAlphabet()), id='2', name='2', description='2', dbxrefs=[]), SeqRecord(seq=Seq('ATACGAATAGCCTATACGTAGCATGCATGGGCTATAATTTTTT', SingleLetterAlphabet()), id='3', name='3', description='3', dbxrefs=[])]

>>> for record in records:
...     print("Record ID:" record.id, "Record Sequence:" record.seq)

Record ID: 1 Record sequence: AGCTAGATCGATGC
Record ID: 2 Record sequence: ATCGATACA
Record ID: 3 Record sequence: ATACGAATAGCCTATACGTAGCATGCATGGGCTATAATTTTTT

{% endhighlight %}

## Manipulating Biopython objects

Working with sequence files can be a bit tricky since all sequences are really Biopython SeqRecord objects. Most sequence processing is done with the sequences converted to *strings*, but to interface with Biopython, we need to convert sequences to SeqRecord objects. 

{% highlight python %}
>>> from Bio.Seq import Seq
>>> from Bio.SeqRecord import SeqRecord
>>> from Bio.Alphabet import *

>>> # Creating a Seq and SeqRecord object
>>> my_sequence = "ACGTACCGTTTTGGAACTTCC"

>>> # Recast to Seq object. Two arguments are the sequence and the alphabet (the latter is optional!!)
>>> my_biopython_seq = Seq(my_sequence, generic_dna)
{% endhighlight %}

Here are some useful methods that you can use on `Seq` objects. Note that all of these methods return other `Seq` objects which can be re-cast to strings with `str()`, if you need.


{% highlight python %}
>>> my_biopython_seq.complement()
Seq('TGCATGGCAAAACCTTGAAGG', DNAAlphabet())
>>> my_biopython_seq.reverse_complement()
Seq('GGAAGTTCCAAAACGGTACGT', DNAAlphabet())
>>> my_biopython_seq.transcribe()
Seq('ACGUACCGUUUUGGAACUUCC', RNAAlphabet())
>>> my_biopython_seq.translate()
Seq('TYRFGTS', ExtendedIUPACProtein())

>>> # Like strings, biopython seq objects are *immutable*
>>> my_biopython_seq[2] = "A"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Seq' object does not support item assignment


>>> # Create a SeqRecord object
>>> my_biopython_seqrec = SeqRecord(my_biopython_seq, id = "seq1") # Can add other arguments as desired
>>> my_biopython_seqrec
SeqRecord(seq=Seq('ACGTACCGTTTTGGAACTTCC', DNAAlphabet()), id='seq1', name='<unknown name>', description='<unknown description>', dbxrefs=[])
{% endhighlight %}



## Writing sequences to file

Biopython supports sequence records to file in a format that you can specify:

{% highlight python %}
>>> # Biopython can write SeqRecord objects to files. Arguments are SeqRecord object(s), file name, sequence format
>>> SeqIO.write(my_biopython_seqrec, "newseq.fasta", "fasta") 

>>> # Write multiple sequences to file by providing SeqIO with a list of SeqRecord objects
>>> rec1 = SeqRecord(my_biopython_seq, id = "seq1")
>>> rec2 = SeqRecord(my_biopython_seq, id = "seq2")
>>> rec3 = SeqRecord(my_biopython_seq, id = "seq3")
>>> lots_of_records = [rec1, rec2, rec3]
>>> SeqIO.write(lots_of_records, "lots_of_records.phy", "phylip")
{% endhighlight %}

<br>
Note that, in many circumstances, it is easiest to write sequences to file using regular file writing, in particular if you want to save in FASTA format. This will require looping over a list (or dictionary!) which contains the sequences to write.
{% highlight python %}
>>> # If sequence_records is a list of biopython objects.
>>> output_file = "sequences.fasta"
>>> with open(output_file, "w") as outf:
...    for record in sequence_records:
...        outf.write(">" + str(record.id) + "\n" + str(record.seq) + "\n")

>>> # If sequence_records is a dictionary containing {id:sequence, id:sequence...}
>>> output_file = "sequences.fasta"
>>> with open(output_file, "w") as outf:
...    for record in sequence_records:
...        outf.write(">" + record + "\n" + sequence_records[record] + "\n")
{% endhighlight %}        


## Converting file formats
Biopython makes it very straight-forward to convert between sequence file formats - simply read in a file and write it out in the new format, or use the handy .convert() method.

{% highlight python %}
>>> # Change file formats
>>> temp = AlignIO.read("file.fasta", "fasta")
>>> AlignIO.write(temp, "newfile.phy", "phylip") #object to write, filename, format 

>>> # Alternatively...
>>> AlignIO.convert("file.fasta", "fasta", "newfile.phy", "phylip")
{% endhighlight %}

## Interacting with sequence alignments

Here are some useful methods for manipulating sequence alignments:

{% highlight python %}
>>> from Bio import AlignIO
>>> aln = AlignIO.read("pb2.fasta", "fasta")
>>> # Use len() to determine alignment size
>>> number_sequences = len(aln)
>>> print number_sequences
400
>>> number_columns = len(aln[0])
>>> print number_columns
2277

>>> # Extract alignment positions
>>> row5_column10_annoying = aln[5].seq[10] 
>>> row5_column10_easier   = aln[5,10]

>>> # Extract alignment columns
>>> col4 = aln[:,4]  # Save alignment column index 4 into a single string
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

>>> Extract alignment regions
>>> aln_chunk = aln[5:10, 9:13] # row indices 5-10 and column indices 9-13
>>> print aln_chunk
SingleLetterAlphabet() alignment with 5 rows and 4 columns
ATAA Av_ABC66491
ATAA Av_CAF33010
ATAA Av_ABI84837
ATAA Av_ABI85028
ATAA Av_ABB19754
{% endhighlight %}

Creating new sequence alignments is a bit tricky - you need to create multiple SeqRecord objects and merge them together into a MultipleSequenceAlignment object. We won't do that here, but you can look it up in the [Biopython tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html).


## Querying online databases

Biopython has excellent built-in tools for collecting and parsing data from NCBI and SwissProt/ExPASy. Here, we'll discuss NCBI querying and parsing. The Biopython online tutorial contains more information about querying and parsing SwissProt information.

### Querying NCBI databases

Any (yes, any!) NCBI database can be queried with the `Entrez` module in Biopython, and you can parse the downloaded data using the `SeqIO` module. As an example, the code below obtains a record for the human hemoglobin alpha subunit gene with ID "NP_000549.1" (note that the GI ID will also work!) from the protein database:

{% highlight python %}
>>> from Bio import Entrez, SeqIO
>>> Entrez.email = "claire.mcwhite@utexas.edu" # Entrez will give you warning messages when a email is not specified. This prevents warnings. Please replace with your email though!!

>>> protein_id = "NP_000549.1"

>>> # Obtain the protein record in a usable format
>>> protein_record_raw = Entrez.efetch(id = protein_id, db = "protein", rettype="gb", retmode="text")
>>> protein_record = SeqIO.read(protein_record_raw, "genbank") 

>>> # You can also save the record to a file:
>>> output_file = protein_id + ".txt"
>>> SeqIO.write(protein_record, output_file, "gb") 
>>> # Read in this data later with SeqIO.read:
>>> record = SeqIO.read(output_file, "gb") 
{% endhighlight %}

Once the record has been parsed by `SeqIO.read()`, we can extract various pieces of information:

{% highlight python %}
>>> # Extract sequence and description attributes
>>> print protein_record.seq
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR
>>> print protein_record.description
hemoglobin subunit alpha [Homo sapiens].

>>> # The .annotations attribute is a dictionary that usually contains a keys like "taxonomy", "organism", "db_source", and "gi": 
>>> print protein_record.annotations["taxonomy"]  # Full list of taxonomic classification
['Eukaryota', 'Metazoa', 'Chordata', 'Craniata', 'Vertebrata', 'Euteleostomi', 'Mammalia', 'Eutheria', 'Euarchontoglires', 'Primates', 'Haplorrhini', 'Catarrhini', 'Hominidae', 'Homo']
>>> print protein_record.annotations["organism"]  # Organism containing this sequence
Homo sapiens
>>> print protein_record.annotations["db_source"]  # Corresponding nucleotide record for this gene
REFSEQ: accession NM_000558.4
>>> print protein_record.annotations["gi"]  # GI accession
4504347
{% endhighlight %}

<br> 
More of the information stored in the `.features` attribute, which is a fairly complicated structure. Each feature contains two important attributes: `type` which indicates the feature we're dealing with, and `qualifiers`, a dictionary of information. To examine this information, you will need to loop over its keys:
{% highlight python %}
>>> features = protein_record.features
>>> for feat in features:
...    print feat.type
...    print feat.qualifiers

source
{'db_xref': ['taxon:9606'], 'organism': ['Homo sapiens'], 'chromosome': ['16'], 'map': ['16p13.3']}
Protein
{'note': ['alpha one globin; hemoglobin alpha 1 globin chain; delta globin; alpha-2 globin chain; hemoglobin, alpha 1'], 'product': ['hemoglobin subunit alpha'], 'calculated_mol_wt': ['15126']}
Site
{'note': ['glycation site'], 'experiment': ['experimental evidence, no additional details recorded'], 'citation': ['[7]', '[9]'], 'site_type': ['glycosylation']}
Region
{'note': ['Hemoglobin alpha, zeta, mu, theta, and related Hb subunits; cd08927'], 'db_xref': ['CDD:271278'], 'region_name': ['Hb-alpha_like']}
Site
{'note': ['Phosphoserine. {ECO:0000244|PubMed:24275569}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['glycation site'], 'experiment': ['experimental evidence, no additional details recorded'], 'citation': ['[9]'], 'site_type': ['glycosylation']}
Site
{'note': ['N6-succinyllysine, alternate. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['modified']}
Site
{'note': ['Phosphothreonine. {ECO:0000244|PubMed:24275569}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['N6-succinyllysine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['modified']}
Site
{'note': ['Not glycated; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['other']}
Site
{'note': ['N6-acetyllysine, alternate. {ECO:0000244|PubMed:19608861}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['acetylation']}
Site
{'note': ['glycation site'], 'experiment': ['experimental evidence, no additional details recorded'], 'citation': ['[7]', '[9]'], 'site_type': ['glycosylation']}
Site
{'note': ['N6-succinyllysine, alternate. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['modified']}
Site
{'note': ['Phosphotyrosine. {ECO:0000244|PubMed:24275569}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'experiment': ['experimental evidence, no additional details recorded'], 'citation': ['[6]'], 'site_type': ['phosphorylation']}
Site
{'note': ['tetramer interface [polypeptide binding]'], 'db_xref': ['CDD:271278'], 'site_type': ['other']}
Site
{'note': ['heme binding site [chemical binding]'], 'db_xref': ['CDD:271278'], 'site_type': ['other']}
Site
{'note': ['Phosphoserine. {ECO:0000244|PubMed:24275569}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['N6-succinyllysine, alternate. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['modified']}
Site
{'experiment': ['experimental evidence, no additional details recorded'], 'citation': ['[6]'], 'site_type': ['phosphorylation']}
Site
{'note': ['Phosphoserine. {ECO:0000244|PubMed:24275569}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['Not glycated; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['other']}
Site
{'note': ['Not glycated; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['other']}
Site
{'note': ['glycation site'], 'experiment': ['experimental evidence, no additional details recorded'], 'citation': ['[7]', '[9]'], 'site_type': ['glycosylation']}
Site
{'note': ['Not glycated; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['other']}
Site
{'note': ['Not glycated; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['other']}
Site
{'note': ['Phosphoserine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['Phosphothreonine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['Phosphoserine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['Phosphoserine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['Phosphothreonine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['Phosphothreonine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
Site
{'note': ['Phosphoserine. {ECO:0000250|UniProtKB:P01942}; propagated from UniProtKB/Swiss-Prot (P69905.2)'], 'experiment': ['experimental evidence, no additional details recorded'], 'site_type': ['phosphorylation']}
CDS
{'coded_by': ['NM_000558.4:67..495'], 'gene': ['HBA1'], 'gene_synonym': ['HBA-T3; HBH'], 'db_xref': ['CCDS:CCDS10399.1', 'GeneID:3039', 'HGNC:HGNC:4823', 'HPRD:00784', 'MIM:141800']}
{% endhighlight %}

<br>
To access a particular feature, such as "CDS" (stands for "CoDing Sequence"), use an `if` statement:

{% highlight python %}
>>> features = protein_record.features
>>> for feat in features:
...    if feat.type == "CDS":
...        print feat.qualifiers

{'coded_by': ['NM_000558.4:67..495'], 'gene': ['HBA1'], 'gene_synonym': ['HBA-T3; HBH'], 'db_xref': ['CCDS:CCDS10399.1', 'GeneID:3039', 'HGNC:HGNC:4823', 'HPRD:00784', 'MIM:141800']}
{% endhighlight %}


The above CDS feature information tells us that the coding sequence record in NCBI for this gene is NM_000558.4, from positions 67-495. It also provides cross-reference information for searching other databases and gene name(s).



Document originally authored by Stephanie Spielman - slightly modified for 2017  by Claire McWhite


