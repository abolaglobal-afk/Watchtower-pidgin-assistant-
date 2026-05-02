#!/usr/bin/env python3
"""
Watchtower Pidgin English Study Assistant

This module provides functionality to manage and display Watchtower study
materials with Pidgin English answers for each paragraph.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
import click


class WatchtowerAssistant:
    """Main class for managing Watchtower study materials in Pidgin English."""
    
    def __init__(self, data_dir: str = "data/watchtower"):
        """
        Initialize the Watchtower Assistant.
        
        Args:
            data_dir (str): Directory containing study JSON files
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def get_study(self, date: str) -> Optional[Dict]:
        """
        Get a complete study for a specific date.
        
        Args:
            date (str): Study date in YYYY-MM-DD format
            
        Returns:
            Dict: Study data or None if not found
        """
        study_file = self.data_dir / f"{date}.json"
        if study_file.exists():
            with open(study_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def get_answer(self, paragraph_num: int, date: str) -> Optional[str]:
        """
        Get the Pidgin English answer for a specific paragraph.
        
        Args:
            paragraph_num (int): Paragraph number (1-18+)
            date (str): Study date in YYYY-MM-DD format
            
        Returns:
            str: Pidgin English answer or None if not found
        """
        study = self.get_study(date)
        if study and 'paragraphs' in study:
            for para in study['paragraphs']:
                if para['number'] == paragraph_num:
                    return para.get('pidgin_answer')
        return None
    
    def get_paragraph(self, paragraph_num: int, date: str) -> Optional[Dict]:
        """
        Get complete information for a specific paragraph.
        
        Args:
            paragraph_num (int): Paragraph number
            date (str): Study date in YYYY-MM-DD format
            
        Returns:
            Dict: Paragraph data including text, answer, and references
        """
        study = self.get_study(date)
        if study and 'paragraphs' in study:
            for para in study['paragraphs']:
                if para['number'] == paragraph_num:
                    return para
        return None
    
    def list_studies(self) -> List[str]:
        """
        List all available study dates.
        
        Returns:
            List[str]: List of available study dates
        """
        studies = []
        for file in self.data_dir.glob("*.json"):
            studies.append(file.stem)
        return sorted(studies)
    
    def get_summary(self, date: str) -> Optional[Dict]:
        """
        Get a summary of the study.
        
        Args:
            date (str): Study date in YYYY-MM-DD format
            
        Returns:
            Dict: Summary including title, theme, and key points
        """
        study = self.get_study(date)
        if not study:
            return None
        
        return {
            'date': study.get('study_date'),
            'title': study.get('title'),
            'subtitle': study.get('subtitle'),
            'theme': study.get('study_theme'),
            'total_paragraphs': len(study.get('paragraphs', [])),
            'opening_comment': study.get('opening_comment'),
            'closing_thoughts': study.get('closing_thoughts')
        }


# CLI Commands
@click.group()
def cli():
    """Watchtower Pidgin Assistant - Study Material Manager"""
    pass


@cli.command()
def list():
    """List all available studies."""
    assistant = WatchtowerAssistant()
    studies = assistant.list_studies()
    
    if not studies:
        click.echo("No studies found. Add JSON files to the data/watchtower/ directory.")
        return
    
    click.echo("Available studies:")
    for study_date in studies:
        click.echo(f"  📅 {study_date}")


@cli.command()
@click.option('--date', required=True, help='Study date (YYYY-MM-DD)')
def view(date):
    """View complete study for a date."""
    assistant = WatchtowerAssistant()
    study = assistant.get_study(date)
    
    if not study:
        click.echo(f"Study not found for date: {date}")
        return
    
    click.echo(f"\n{'='*60}")
    click.echo(f"📖 {study.get('title', 'Untitled')}")
    click.echo(f"{'='*60}")
    click.echo(f"Date: {study.get('study_date')}")
    click.echo(f"Subtitle: {study.get('subtitle', 'N/A')}")
    click.echo(f"\nTheme: {study.get('study_theme', 'N/A')}")
    click.echo(f"\nOpening: {study.get('opening_comment', 'N/A')}\n")
    
    for para in study.get('paragraphs', []):
        click.echo(f"\n{'─'*60}")
        click.echo(f"Paragraph {para['number']}")
        click.echo(f"{'─'*60}")
        click.echo(f"📝 Text: {para.get('text', 'N/A')}")
        click.echo(f"\n🇳🇬 Pidgin Answer:\n{para.get('pidgin_answer', 'N/A')}")
        
        if para.get('key_points'):
            click.echo("\n✨ Key Points:")
            for point in para['key_points']:
                click.echo(f"  • {point}")
        
        if para.get('cross_references'):
            click.echo("\n📌 Bible References:")
            for ref in para['cross_references']:
                click.echo(f"  ➜ {ref}")
    
    click.echo(f"\n\nClosing: {study.get('closing_thoughts', 'N/A')}")
    click.echo(f"\n{'='*60}\n")


@cli.command()
@click.option('--paragraph', type=int, required=True, help='Paragraph number')
@click.option('--date', required=True, help='Study date (YYYY-MM-DD)')
def answer(paragraph, date):
    """Get the Pidgin English answer for a paragraph."""
    assistant = WatchtowerAssistant()
    pidgin_answer = assistant.get_answer(paragraph, date)
    
    if not pidgin_answer:
        click.echo(f"Answer not found for paragraph {paragraph} on {date}")
        return
    
    click.echo(f"\n{'='*60}")
    click.echo(f"Paragraph {paragraph} - {date}")
    click.echo(f"{'='*60}")
    click.echo(f"\n🇳🇬 Pidgin Answer:\n{pidgin_answer}\n")


@cli.command()
@click.option('--date', required=True, help='Study date (YYYY-MM-DD)')
def summary(date):
    """Get a summary of the study."""
    assistant = WatchtowerAssistant()
    summary_data = assistant.get_summary(date)
    
    if not summary_data:
        click.echo(f"Study not found for date: {date}")
        return
    
    click.echo(f"\n{'='*60}")
    click.echo(f"📖 Study Summary - {summary_data['date']}")
    click.echo(f"{'='*60}")
    click.echo(f"Title: {summary_data['title']}")
    click.echo(f"Subtitle: {summary_data['subtitle']}")
    click.echo(f"Theme: {summary_data['theme']}")
    click.echo(f"Total Paragraphs: {summary_data['total_paragraphs']}")
    click.echo(f"\nOpening: {summary_data['opening_comment']}")
    click.echo(f"\nClosing Thoughts: {summary_data['closing_thoughts']}\n")


if __name__ == '__main__':
    cli()
