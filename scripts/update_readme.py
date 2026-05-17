#!/usr/bin/env python3
"""
Script to automatically update README.md with latest information.
This script is called by the GitHub Actions workflow.
"""

import os
import re
from datetime import datetime

def update_readme_timestamp():
    """Update the timestamp in README.md"""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Update the timestamp
        current_time = datetime.utcnow().strftime("%Y-%m-%d")
        timestamp_pattern = r"(> \*\*Last Updated:\*\*) [\d\-]+"
        updated_content = re.sub(
            timestamp_pattern,
            f"\\1 {current_time}",
            content
        )
        
        if updated_content != content:
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(updated_content)
            print("✅ README.md timestamp updated successfully")
            return True
        else:
            print("ℹ️ No timestamp changes needed")
            return False
            
    except Exception as e:
        print(f"❌ Error updating README: {e}")
        return False

def add_github_stats():
    """
    Placeholder for fetching and adding GitHub stats.
    Can be extended to fetch actual stats from GitHub API.
    """
    try:
        print("ℹ️ GitHub stats placeholder - ready for expansion")
        # Future: Add actual GitHub API calls here
        return True
    except Exception as e:
        print(f"⚠️ Error adding GitHub stats: {e}")
        return False

def main():
    """Main function to run all update tasks"""
    print("🚀 Starting README update process...")
    print(f"⏰ Execution time: {datetime.utcnow().isoformat()}")
    
    tasks = [
        ("Updating timestamp", update_readme_timestamp),
        ("Adding GitHub stats", add_github_stats),
    ]
    
    results = []
    for task_name, task_func in tasks:
        try:
            print(f"\n📝 {task_name}...")
            result = task_func()
            results.append((task_name, result))
        except Exception as e:
            print(f"❌ {task_name} failed: {e}")
            results.append((task_name, False))
    
    print("\n" + "="*50)
    print("📊 Update Summary:")
    for task_name, result in results:
        status = "✅" if result else "⚠️"
        print(f"  {status} {task_name}")
    print("="*50)

if __name__ == "__main__":
    main()
