function App() {
  return (
    <div style={styles.page}>
      <nav style={styles.navbar}>
        <div style={styles.logo}>🎬 MoodFlix</div>

        <div style={styles.menu}>
          <button style={styles.navButton}>🏠 Home</button>
          <button style={styles.navButton}>🤖 AI Mood</button>
          <button style={styles.navButton}>🔥 Trending</button>
          <button style={styles.navButton}>😊 Feel Good</button>
          <button style={styles.navButton}>💕 Date Night</button>
          <button style={styles.navButton}>🚀 Motivation Hub</button>
          <button style={styles.navButton}>🔤 Browse A-Z</button>
        </div>
      </nav>

      <section style={styles.hero}>
        <div style={styles.overlay}>
          <h1 style={styles.title}>Discover Movies Based On Your Mood</h1>

          <p style={styles.subtitle}>
            MoodFlix combines AI and movie recommendations to help you find the perfect movie for every feeling.
          </p>

          <div>
            <button style={styles.playButton}>▶ Start Exploring</button>
            <button style={styles.infoButton}>ℹ AI Mood</button>
          </div>
        </div>
      </section>

      <section style={styles.trendingSection}>
        <h2 style={styles.sectionTitle}>🔥 Trending Now</h2>

        <div style={styles.movieRow}>
          <div style={styles.movieCard}>
            <img
              src="https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
              style={styles.poster}
            />
            <p>Interstellar</p>
          </div>

          <div style={styles.movieCard}>
            <img
              src="https://image.tmdb.org/t/p/w500/p2lVAcPuRPSO8Al6hDDGw0OgMi8.jpg"
              style={styles.poster}
            />
            <p>Dangal</p>
          </div>

          <div style={styles.movieCard}>
            <img
              src="https://image.tmdb.org/t/p/w500/vpbaStTMt8qqXaEgnOR2EE4DNJk.jpg"
              style={styles.poster}
            />
            <p>Up</p>
          </div>

          <div style={styles.movieCard}>
            <img
              src="https://image.tmdb.org/t/p/w500/cqxg1CihGR5ge0i1wYXr4Rdeppu.jpg"
              style={styles.poster}
            />
            <p>Rocky</p>
          </div>
        </div>
      </section>
    </div>
  )
}

const styles = {
  page: {
    backgroundColor: "#0b0b0b",
    minHeight: "100vh",
    color: "white",
    padding: "30px",
    fontFamily: "Arial, sans-serif"
  },

  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    gap: "20px"
  },

  logo: {
    fontSize: "34px",
    fontWeight: "900",
    color: "#e50914"
  },

  menu: {
    display: "flex",
    gap: "10px",
    flexWrap: "wrap"
  },

  navButton: {
    background: "#1f1f1f",
    color: "white",
    border: "1px solid #333",
    padding: "10px 14px",
    borderRadius: "8px",
    cursor: "pointer"
  },

  hero: {
    marginTop: "60px",
    height: "500px",
    borderRadius: "20px",
    backgroundImage:
      "url('https://image.tmdb.org/t/p/original/56v2KjBlU4XaOv9rVYEQypROD7P.jpg')",
    backgroundSize: "cover",
    backgroundPosition: "center",
    display: "flex",
    alignItems: "center",
    overflow: "hidden"
  },

  overlay: {
    width: "100%",
    height: "100%",
    background:
      "linear-gradient(to right, rgba(0,0,0,.95), rgba(0,0,0,.25))",
    padding: "80px",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center"
  },

  title: {
    fontSize: "64px",
    maxWidth: "800px",
    marginBottom: "20px"
  },

  subtitle: {
    fontSize: "22px",
    color: "#cccccc",
    maxWidth: "650px",
    lineHeight: "1.5"
  },

  playButton: {
    marginTop: "35px",
    marginRight: "16px",
    padding: "15px 28px",
    fontSize: "18px",
    fontWeight: "700",
    borderRadius: "8px",
    border: "none",
    cursor: "pointer"
  },

  infoButton: {
    padding: "15px 28px",
    fontSize: "18px",
    fontWeight: "700",
    borderRadius: "8px",
    border: "none",
    background: "rgba(255,255,255,.25)",
    color: "white",
    cursor: "pointer"
  },

  trendingSection: {
    marginTop: "60px"
  },

  sectionTitle: {
    fontSize: "40px",
    marginBottom: "30px"
  },

  movieRow: {
    display: "flex",
    gap: "30px",
    overflowX: "auto"
  },

  movieCard: {
    minWidth: "200px",
    cursor: "pointer"
  },

  poster: {
    width: "200px",
    height: "300px",
    objectFit: "cover",
    borderRadius: "12px"
  }
}

export default App