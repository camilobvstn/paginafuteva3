"use client";
import React, { useState, useEffect } from "react";

function FormPartido() {
  // Estados para cada campo
  const [nombrelocal, setNombrelocal] = useState("");
  const [nombrevisita, setNombrevisita] = useState("");
  const [fecha, setFecha] = useState("");
  const [horapartido, setHorapartido] = useState("");
  const [logolocal, setLogolocal] = useState(null);
  const [logovisita, setLogovisita] = useState(null);
  const [partidos, setPartidos] = useState([]);
  const [partidoActualizarId, setPartidoActualizarId] = useState(null);

  // Cargar partidos registrados
  useEffect(() => {
    const fetchPartidos = async () => {
      try {
        const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/partidoapi/`);
        const data = await res.json();
        setPartidos(data);
      } catch {
        alert("Hubo un error al cargar los partidos");
      }
    };

    fetchPartidos();
  }, []);

  const handleChange = (e) => {
    const { name, value, type, files } = e.target;
    if (type === "file") {
      if (name === "logolocal") setLogolocal(files[0]);
      if (name === "logovisita") setLogovisita(files[0]);
    } else {
      if (name === "nombrelocal") setNombrelocal(value);
      if (name === "nombrevisita") setNombrevisita(value);
      if (name === "fecha") setFecha(value);
      if (name === "horapartido") setHorapartido(value);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const formData = new FormData();
    formData.append("nombrelocal", nombrelocal);
    formData.append("nombrevisita", nombrevisita);
    formData.append("fecha", fecha);
    formData.append("horapartido", horapartido);
    if (logolocal) formData.append("logolocal", logolocal);
    if (logovisita) formData.append("logovisita", logovisita);
  
    try {
      let res;
      if (partidoActualizarId) {
        // Actualizar partido
        res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/partidoapi/${partidoActualizarId}/`, {
          method: "PUT",
          body: formData,
        });
      } else {
        // Registrar nuevo partido
        res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/partidoapi/`, {
          method: "POST",
          body: formData,
        });
      }

      const data = await res.json();
      alert(partidoActualizarId ? "Partido actualizado correctamente" : "Partido registrado correctamente");

      if (partidoActualizarId) {
        setPartidos(partidos.map((partido) => (partido.id === partidoActualizarId ? data : partido)));
      } else {
        setPartidos((prevPartidos) => [...prevPartidos, data]);
      }

      setNombrelocal("");
      setNombrevisita("");
      setFecha("");
      setHorapartido("");
      setLogolocal(null);
      setLogovisita(null);
      setPartidoActualizarId(null); // Limpiar el ID de actualización
    } catch {
      alert("Hubo un error al registrar o actualizar el partido");
    }
  };

  const handleUpdate = (id) => {
    const partidoToUpdate = partidos.find((partido) => partido.id === id);
    setNombrelocal(partidoToUpdate.nombrelocal);
    setNombrevisita(partidoToUpdate.nombrevisita);
    setFecha(partidoToUpdate.fecha);
    setHorapartido(partidoToUpdate.horapartido);
    setPartidoActualizarId(id); // Guardar el ID del partido a actualizar
  };

  const handleDelete = async (id) => {
    try {
      await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/partidoapi/${id}/`, {
        method: "DELETE",
      });

      setPartidos(partidos.filter((partido) => partido.id !== id));
      alert("Partido eliminado correctamente");
    } catch {
      alert("Hubo un error al eliminar el partido");
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto bg-white shadow-lg rounded-lg">
      <form onSubmit={handleSubmit} encType="multipart/form-data" className="space-y-4">
        <div>
          <h1>Formulario de partidos</h1>
          <label htmlFor="nombrelocal" className="block font-medium text-gray-700">Nombre Local:</label>
          <input
            type="text"
            id="nombrelocal"
            name="nombrelocal"
            value={nombrelocal}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded-md"
            required
          />
        </div>
        <div>
          <label htmlFor="nombrevisita" className="block font-medium text-gray-700">Nombre Visita:</label>
          <input
            type="text"
            id="nombrevisita"
            name="nombrevisita"
            value={nombrevisita}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded-md"
            required
          />
        </div>
        <div>
          <label htmlFor="fecha" className="block font-medium text-gray-700">Fecha:</label>
          <input
            type="date"
            id="fecha"
            name="fecha"
            value={fecha}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded-md"
            required
          />
        </div>
        <div>
          <label htmlFor="horapartido" className="block font-medium text-gray-700">Hora del Partido:</label>
          <input
            type="time"
            id="horapartido"
            name="horapartido"
            value={horapartido}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded-md"
            required
          />
        </div>
        <div>
          <label htmlFor="logolocal" className="block font-medium text-gray-700">Logo Local:</label>
          <input
            type="file"
            id="logolocal"
            name="logolocal"
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div>
          <label htmlFor="logovisita" className="block font-medium text-gray-700">Logo Visita:</label>
          <input
            type="file"
            id="logovisita"
            name="logovisita"
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white p-2 rounded-md mt-4 hover:bg-blue-600"
        >
          {partidoActualizarId ? "Actualizar Partido" : "Registrar Partido"}
        </button>
      </form>

      <h2 className="mt-6 text-xl font-semibold">Partidos Registrados</h2>
      <ul className="space-y-4 mt-4">
        {partidos.map((partido) => (
          <li key={partido.id} className="p-4 border border-gray-300 rounded-md flex justify-between items-center">
            <div>
              <span className="font-medium">{partido.nombrelocal}</span> vs <span className="font-medium">{partido.nombrevisita}</span>
              <div className="text-gray-500">{partido.fecha} a las {partido.horapartido}</div>
            </div>
            <div className="space-x-2">
              <button
                onClick={() => handleUpdate(partido.id)}
                className="bg-yellow-500 text-white px-4 py-2 rounded-md hover:bg-yellow-600"
              >
                Actualizar
              </button>
              <button
                onClick={() => handleDelete(partido.id)}
                className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600"
              >
                Eliminar
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FormPartido;
