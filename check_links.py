import re
import requests
from pathlib import Path
import time

# Replacement links for common broken URLs
REPLACEMENTS = {
    # Khan Academy alternatives
    'electric-field-intensity': 'https://www.khanacademy.org/science/physics/electric-charge-electric-force-and-voltage/electric-field/v/electric-field-direction',
    
    # YouTube alternatives
    'FXfWXxnT6Qs': 'https://www.youtube.com/watch?v=x4SLkVJ8e1E',  # Electric field superposition
    'FhwlfPMJgm4': 'https://www.youtube.com/watch?v=w82aSjLuD_8',  # Power in circuits
    'TdUK6RPdIrA': 'https://www.youtube.com/watch?v=SLkGpTjalzM',  # Using multimeters
    '3H6Rttqx0Yw': 'https://www.youtube.com/watch?v=3H6Rttqx0Yw',  # KVL
    'YZRjVnZJZGw': 'https://www.youtube.com/watch?v=yz5ftjt6GWE',  # Internal resistance
    '9g9LkgY_5Hs': 'https://www.youtube.com/watch?v=f_MZNsEqyQw',  # RC circuits
}

def extract_urls_from_file(filepath):
    """Extract all URLs from a flashcards file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all [RESOURCE:...] URL patterns
    pattern = r'\[RESOURCE:[^\]]+\]\s+(https?://[^\s\n]+)'
    matches = re.findall(pattern, content)
    return matches

def check_url(url, timeout=10):
    """Check if a URL is accessible"""
    try:
        # Use HEAD request for faster checking
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        if response.status_code == 405:  # Method not allowed, try GET
            response = requests.get(url, timeout=timeout, allow_redirects=True)
        return response.status_code < 400
    except Exception as e:
        print(f"  ❌ Error checking {url}: {str(e)[:50]}")
        return False

def main():
    quiz_dirs = [
        Path('tests/Quiz 2 V1'),
        Path('tests/Quiz 2 V2'),
        Path('tests/Quiz 2 V3')
    ]
    
    all_results = {}
    
    for quiz_dir in quiz_dirs:
        flashcard_file = quiz_dir / 'flashcards.txt'
        if not flashcard_file.exists():
            continue
            
        print(f"\n{'='*60}")
        print(f"Checking {quiz_dir.name}")
        print('='*60)
        
        urls = extract_urls_from_file(flashcard_file)
        print(f"Found {len(urls)} resource links")
        
        results = []
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Checking: {url[:70]}...")
            is_valid = check_url(url)
            
            if is_valid:
                print("  ✅ Valid")
            else:
                print("  ❌ Broken")
                # Suggest replacement
                for key, replacement in REPLACEMENTS.items():
                    if key in url:
                        print(f"  💡 Suggested replacement: {replacement}")
                        break
            
            results.append({
                'url': url,
                'valid': is_valid
            })
            
            # Be nice to servers
            time.sleep(0.5)
        
        all_results[str(quiz_dir)] = results
        
        # Summary
        valid_count = sum(1 for r in results if r['valid'])
        broken_count = len(results) - valid_count
        print(f"\n📊 Summary for {quiz_dir.name}:")
        print(f"  ✅ Valid: {valid_count}")
        print(f"  ❌ Broken: {broken_count}")
    
    # Overall summary
    print(f"\n{'='*60}")
    print("OVERALL SUMMARY")
    print('='*60)
    for quiz, results in all_results.items():
        valid = sum(1 for r in results if r['valid'])
        total = len(results)
        print(f"{quiz}: {valid}/{total} valid ({100*valid//total}%)")

if __name__ == '__main__':
    main()
