# ETL Pipeline for Search Systems

## What You're Actually Presenting On

Based on research, the "intelligence layer" maps to established data engineering patterns.

---

## Your "Intelligence Layer" = Industry Terms

| What You Call It | Industry Terms | What You Built |
|------------------|----------------|----------------|
| Intelligence Layer | ETL/Data Pipeline | Extract from API → Transform → Load to search |
| Change Detection | Incremental Loading / CDC | Hash-based deduplication |
| Cross-Document Aggregation | Data Denormalization | Leader specialties → team pages |
| Background Jobs | State Management | Batch processing with offset tracking |
| Feature Extraction | Semantic Layer | Specialties, privacy flags, employment status |

---

## Industry Concepts Breakdown

### 1. **ETL/Data Pipeline for Search**
The process of extracting data from source systems, transforming it, and loading it into your search engine.

**What you built:**
- Extract: API calls to `ttiAPI_cached_employee_list()` and `ttiAPI_cached_resume()`
- Transform: Data cleaning, denormalization, feature extraction
- Load: Batch indexing into staff_directory CPT for Relevanssi

### 2. **Incremental Loading / Change Data Capture (CDC)**
Only processing data that has changed since the last run.

**Industry methods:**
- **Timestamp-based**: Track `updated_at` columns
- **Change Data Capture (CDC)**: Capture changes from database logs
- **Hashing**: Create checksums to detect changes

**What you built:** Hash-based change detection using `md5(serialize($data))`

### 3. **Data Denormalization for Search**
Flattening relational data into search-optimized documents.

**Why denormalization matters:**
- Search engines like Elasticsearch/Algolia work best with flat documents, not joins
- Denormalization combines related data into single records for fast retrieval
- Essential for analytical systems (OLAP) vs. transactional databases (OLTP)

**What you built:** Cross-document feature aggregation (rolling up leader specialties to team pages)

### 4. **State Management & Idempotency**
Ensuring pipelines can resume after failures and don't create duplicates.

**Best practices:**
- **State tracking**: Store timestamps or offsets of last successful run
- **Idempotency**: Processing the same data twice produces the same result
- **Checkpointing**: Resume from last successful state

**What you built:** Batch processing with offset tracking (`staff_index_offset` option)

### 5. **Semantic Layer** (Emerging 2026 Trend)
Standardizing business definitions and adding context to data.

**What it is:**
- Metadata-driven architectures enabling automation and intelligence across data ecosystems
- Standardizes business definitions and metrics for consistency across reports and AI models
- "AI initiatives struggle not because of a lack of intelligence, but because they lack business context"

**What you built:** Feature extraction (specialties, org, title) with business context (privacy flags, employment status)

---

## The Talk Framework (Industry-Grounded)

### Title Options:
1. **"The ETL Pipeline Nobody Talks About: Preparing Data for Search"**
2. **"Before You Query: Building the Data Pipeline Layer for Search Systems"**
3. **"From Messy APIs to Clean Search: An ETL Story"**
4. **"Change Detection, Denormalization, and Other Search Pipeline Problems"**

### Structure:

**Act 1: The Problem**
- Staff discovery in a research org
- Data comes from multiple APIs (employee list, resumes)
- Need to make it searchable

**Act 2: The ETL Pipeline (What You Built)**
1. **Extract** - API calls, caching strategies
2. **Transform** - Data cleaning, feature extraction, denormalization
3. **Load** - Batch indexing with change detection
4. **Orchestration** - WP-CLI + cron scheduling

**Act 3: The Patterns (Industry Practices)**
1. **Incremental loading** - Hash-based vs. timestamp-based vs. CDC
2. **Denormalization** - Why search engines need flat documents
3. **State management** - Offset tracking, idempotency, checkpointing
4. **Semantic layer** - Adding business context (privacy, employment status)

**Act 4: The Lessons**
1. Change detection saves processing time and money
2. Denormalization is mandatory for search (no joins)
3. State management prevents duplicate work
4. The "intelligence" is in the transformation logic, not the search engine

---

## Key Takeaway

**You're not inventing new concepts. You're applying standard data engineering practices (ETL, incremental loading, denormalization) to the search domain.**

The value of your talk is:
- ✅ Showing **practical implementation** of these patterns
- ✅ Demonstrating the **problems** that force you to build this layer
- ✅ Sharing **real code** (hash generation, batch processing, cross-document aggregation)
- ✅ Explaining **why** these patterns matter for search (not just theory)

---

## Sources

**Data Pipelines & Intelligence:**
- [How to Build Modern Data Pipelines for Analytics and AI in 2026](https://www.alation.com/blog/building-data-pipelines/)
- [Data Engineering Trends 2026 for AI-Driven Enterprises](https://www.trigyn.com/insights/data-engineering-trends-2026-building-foundation-ai-driven-enterprises)
- [4 trends that will shape data management and AI in 2026](https://www.techtarget.com/searchdatamanagement/feature/4-trends-that-will-shape-data-management-and-AI-in-2026)

**Incremental Loading & Change Detection:**
- [Incremental Load Strategy for Data Warehouses (2025 Guide)](https://blog.skyvia.com/incremental-load-strategy-for-data-warehouses/)
- [Data Engineering: Incremental Data Loading Strategies](https://dataengineeracademy.com/blog/data-engineering-incremental-data-loading-strategies/)
- [Building Efficient Data Pipelines With Incremental Updates](https://www.fivetran.com/blog/building-efficient-data-pipelines-with-incremental-updates)
- [Best Practices for Managing Cloud-based Incremental Data Loads](https://www.clicdata.com/blog/incremental-data-loads/)

**Denormalization & ETL:**
- [What role does normalization or denormalization play in ETL transformations?](https://milvus.io/ai-quick-reference/what-role-does-normalization-or-denormalization-play-in-etl-transformations)
- [What Is An ETL Pipeline? Process & Tools Guide 2026](https://skyvia.com/learn/etl-pipeline-meaning)

**Search Indexing:**
- [Inside the Algolia Engine: Indexing vs. Search](https://www.algolia.com/blog/engineering/inside-the-algolia-engine-part-1-indexing-vs-search)
- [An Exploration of Search and Indexing: Fast Indexing Scenarios](https://www.algolia.com/blog/product/an-exploration-of-search-and-indexing-real-time-indexing-scenarios)
