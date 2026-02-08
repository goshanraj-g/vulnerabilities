/**
 * Cross-Site Scripting (XSS) Vulnerability Examples
 * ==================================================
 * EDUCATIONAL PURPOSE ONLY - DO NOT USE IN PRODUCTION
 * 
 * This script demonstrates various XSS vulnerabilities where user input
 * is rendered without proper sanitization.
 */

// VULNERABLE: Reflected XSS
function vulnerableSearch(searchQuery) {
    /**
     * VULNERABLE: User input directly inserted into HTML
     * Attack: <script>alert('XSS')</script>
     */
    document.getElementById('results').innerHTML = 
        `<h2>Search results for: ${searchQuery}</h2>`;
    console.log('[VULNERABLE] Reflected XSS - unescaped user input in HTML');
}

// VULNERABLE: Stored XSS
class VulnerableCommentSystem {
    constructor() {
        this.comments = [];
    }
    
    addComment(username, comment) {
        /**
         * VULNERABLE: Stores unsanitized user input
         * Attack: <img src=x onerror="alert('Stored XSS')">
         */
        this.comments.push({ username, comment });
        this.renderComments();
    }
    
    renderComments() {
        const commentSection = document.getElementById('comments');
        let html = '<div class="comment-list">';
        
        // VULNERABLE CODE - Direct HTML insertion
        this.comments.forEach(c => {
            html += `
                <div class="comment">
                    <strong>${c.username}</strong>: ${c.comment}
                </div>
            `;
        });
        
        html += '</div>';
        commentSection.innerHTML = html; // XSS vulnerability here
        console.log('[VULNERABLE] Stored XSS - unsanitized stored data');
    }
}

// VULNERABLE: DOM-based XSS
function vulnerableUrlParameter() {
    /**
     * VULNERABLE: Reading and rendering URL parameters without sanitization
     * Attack URL: page.html?message=<script>alert('DOM XSS')</script>
     */
    const urlParams = new URLSearchParams(window.location.search);
    const message = urlParams.get('message');
    
    if (message) {
        // VULNERABLE CODE
        document.getElementById('welcome').innerHTML = 
            `<h1>Welcome! ${message}</h1>`;
        console.log('[VULNERABLE] DOM-based XSS - unsanitized URL parameter');
    }
}

// VULNERABLE: JavaScript execution via eval
function vulnerableCalculator(expression) {
    /**
     * VULNERABLE: Using eval with user input
     * Attack: "alert('XSS via eval')"
     */
    try {
        const result = eval(expression); // NEVER DO THIS
        console.log(`[VULNERABLE] Eval XSS - Result: ${result}`);
        return result;
    } catch (e) {
        console.error('Error:', e);
    }
}

// VULNERABLE: innerHTML with event handlers
function vulnerableProfileUpdate(bio) {
    /**
     * VULNERABLE: Event handler injection
     * Attack: <div onmouseover="alert('XSS')">Hover me</div>
     */
    document.getElementById('user-bio').innerHTML = bio;
    console.log('[VULNERABLE] Event handler injection in innerHTML');
}

// Example attacks demonstration
console.log('=== XSS Vulnerability Examples ===\n');

// Example 1: Reflected XSS attack payloads
console.log('1. Reflected XSS Attack Payloads:');
const xssPayloads = [
    '<script>alert("XSS")</script>',
    '<img src=x onerror="alert(\'XSS\')">',
    '<svg onload="alert(\'XSS\')">',
    '<iframe src="javascript:alert(\'XSS\')"></iframe>'
];
console.log(xssPayloads);

// Example 2: Stored XSS
console.log('\n2. Stored XSS Example:');
const commentSystem = new VulnerableCommentSystem();
console.log('Adding malicious comment...');

// Example 3: DOM XSS
console.log('\n3. DOM-based XSS:');
console.log('Attack URL: index.html?message=<script>alert("XSS")</script>');

// Example 4: eval() vulnerability
console.log('\n4. Eval XSS:');
console.log('Input: document.cookie');

console.log('\n=== SECURE ALTERNATIVES ===');
console.log('1. Use textContent instead of innerHTML for text');
console.log('2. Use DOMPurify or similar libraries to sanitize HTML');
console.log('3. Use Content Security Policy (CSP) headers');
console.log('4. Encode output based on context (HTML, JS, URL)');
console.log('5. NEVER use eval() with user input');
console.log('6. Use modern frameworks with auto-escaping (React, Vue, Angular)');

// Secure alternative example
function secureSearch(searchQuery) {
    /**
     * SECURE: Using textContent to prevent XSS
     */
    const results = document.getElementById('results');
    const heading = document.createElement('h2');
    heading.textContent = `Search results for: ${searchQuery}`;
    results.innerHTML = ''; // Clear first
    results.appendChild(heading);
    console.log('[SECURE] Used textContent - no XSS possible');
}
