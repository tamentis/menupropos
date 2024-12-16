#!/usr/bin/env python

import base64
import os
import sys
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = (
    "Extract and format the text from this image into Markdown format. "
    "Assume these are pages from a book, so you should join paragraph lines properly when needed instead of keeping the lines as-is. "
    "Please ignore page numbers, and the upper-cased text on the same line as the page number, which is the title of the book and the title of the current chapter. "
)


def ocr_to_markdown(image_path):
    """
    Sends an image to OpenAI's OCR model (o1) and retrieves Markdown-formatted text.
    """
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ]

        try:
            response = client.chat.completions.create(
                model="gpt-4o", messages=messages, max_tokens=600
            )

            # response = client.images.generate(
            #     model="o1",
            #     file=image_file,
            #     purpose="OCR",
            #     prompt="",
            # )
            # Extract text from the response
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return None


def process_image(filename):
    """
    Processes all images in the input folder and saves OCR results as Markdown files.
    """
    if filename.lower().endswith((".jpg", ".jpeg")):
        output_md_file_path = f"{filename}.md"

        # Perform OCR
        markdown_text = ocr_to_markdown(filename)

        if markdown_text:
            # Save the result to a Markdown file
            with open(output_md_file_path, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_text)
        else:
            print(f"Failed to process: {filename}")


# Run the process
process_image(sys.argv[1])
