import json 
import os 
import sys

RESULTING_README = ""

# adding about section
ABOUT_SECTION = "# About \n\
Just to make it convenient for me and (possibly) for other folks I'll store some info about \
papers I've read. Moreover, I would like to use this repo as some kind of papers waiting-list, \
just to manage reading pipeline consistent. \n \
"

RESULTING_README += ABOUT_SECTION 

# loading jsons papers collection
PAPERS_DIR = "papers_db"
papers_descriptions = os.listdir(PAPERS_DIR)
papers_descriptions = [json.load(open(os.path.join(PAPERS_DIR, p))) for p in papers_descriptions]

unique_tags = {tag for paper_sample in papers_descriptions for tag in paper_sample["tags"]}

# adding content description
CONTENT = "## Content \n"
for tag in unique_tags:
	tag_name = "-".join(tag.lower().split())
	CONTENT += f"- [{tag}](#{tag_name})\n"
CONTENT += "\n****\n"

RESULTING_README += CONTENT 

def process_paper(sample):

	resulting_line = ""
	resulting_line += f'[added : {sample["dateAdded"]}] [done: {sample["dateDone"]}]\n'
	resulting_line += f'* {sample["title"]}'

	if sample["pdf"]:
		resulting_line += f' [[pdf]]({sample["pdf"]}) '

	if  sample["code"]:
		resulting_line += f' [[code]]({sample["code"]}) '

	if sample["videos"]:
		for i, video in enumerate(sample["videos"]):
			resulting_line += f' [[video{i}]]({video}) '

	resulting_line += "\n"
	
	resulting_line += r"* \- "
	for author in sample["authors"]:
		resulting_line += f'{author} - '
	resulting_line += "\n"

	resulting_line += f'* `{sample["place"]}`\n'

	tags_line = "* "
	for tag in sample["tags"]: 
		tag_name = "-".join(tag.lower().split())
		tags_line += f'[[{tag}]](#{tag_name}) '
	resulting_line += tags_line + "\n"

	# adding comments for paper 
	for i, comment in enumerate(sample["comments"]):
		comment_formating = f'<details>\n  <summary> Comment {i+1}</summary> {comment}\n </details>\n'
		resulting_line += comment_formating

	return resulting_line

# adding different sections by tags
for tag in sorted(unique_tags):
	tagged_papers = [paper for paper in papers_descriptions if tag in paper['tags']]
	RESULTING_README += f"### {tag} (#papers = {len(tagged_papers)})\n\n"
	# TODO sort in order of adding date
	for paper in sorted(tagged_papers, key=lambda x: x["title"]):
		RESULTING_README += process_paper(paper) + "\n"
	RESULTING_README += "\n***\n"


open("./RM.md", "w").write(RESULTING_README)